import pandas as pd
import yfinance as yf
import datetime
import sys
import csv


# TECHNICAL ANALYSIS INDICATORS FOR TRADING
# LUIZ GUSTAVO BARICHELLO
## CATALAO, GOIAS, BRAZIL


def main():
    # Get input from the user
    input_n = 0
    while input_n not in [1, 2, 3]:
        input_n = int(
            input(
                "Specify the number that represents you input: \n1: Excel File \n2: Csv File \n3: Manual input \n-> "
            )
        )

    # If Excel File
    if input_n == 1:
        filepath = input("Type the name of the file you want to be read: ").strip()

        # List of accepted formats
        accepted_formats = [".xls", ".xlsx", ".xlsm", ".xlsb", ".odf", ".ods", ".odt"]

        # If the input is in the list, continue; if not, exit
        for format in accepted_formats:
            if filepath.endswith(format):
                break
        else:
            print("Invalid format for excel file.")
            sys.exit(1)

        # Try to read the file
        try:
            excel_list = pd.read_excel(filepath, usecols=[0, 0])
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

        ticker_list = excel_list["Ticker"].values.tolist()

    # If CSV File
    elif input_n == 2:
        filepath = input("Type the name of the file you want to be read: ").strip()

        if not filepath.endswith(".csv"):
            print("Invalid format for CSV file.")
            sys.exit(1)

        with open(f"{filepath}", newline="") as file:
            reader = csv.reader(file)
            ticker_list = [row for row in reader]
            ticker_list = ticker_list[0]

    # If manual input
    else:
        print("Type one ticker at a time and 'Done!' when you are done.")
        ticker_list = []

        while True:
            ticker_input = input("Ticker: ").strip()

            if ticker_input == "Done!":
                break

            ticker_list.append(ticker_input)

    # Output File
    filepath_out = input("Type the name of the file you want output: ").strip()

    # Search period
    days_ago = int(
        input("From how many days ago you want to download your data: ").strip()
    )
    end_dt = datetime.datetime.now()
    start_dt = end_dt - datetime.timedelta(days=days_ago)

    # Download data from yahoo
    data = yf.download(
        ticker_list, start_dt, end_dt, back_adjust=True, auto_adjust=True
    )

    # Correct data
    data = data.dropna(axis=1, how="all")
    data = data.fillna(method="pad")

    # Separate all data into sections
    closes = data["Close"].copy()
    opens = data["Open"].copy()
    highs = data["High"].copy()
    lows = data["Low"].copy()
    volume = data["Volume"].copy()

    # Getting indicator data
    ema9 = moving_average(closes, 9, "EMA")
    sma200 = moving_average(closes, 200, "SMA")
    inside_bars = price_action(closes, opens, highs, lows, "inside bar")
    outside_bars = price_action(closes, opens, highs, lows, "outside bar")
    candle_of_force = price_action(closes, opens, highs, lows, "candle of force")
    upper_shadow = price_action(closes, opens, highs, lows, "upper shadow")
    lower_shadow = price_action(closes, opens, highs, lows, "lower shadow")
    rsi14 = rsi(closes, 14)

    # Outputting to excel
    filepath_out = filepath_out.split(".")
    with pd.ExcelWriter(f"{filepath_out[0]}.xlsx") as writer:
        data.reindex(index=data.index[::-1]).to_excel(writer, sheet_name="Data")
        ema9.to_excel(writer, sheet_name="EMA 9")
        sma200.to_excel(writer, sheet_name="SMA 200")
        inside_bars.to_excel(writer, sheet_name="Inside Bars")
        outside_bars.to_excel(writer, sheet_name="Outside Bars")
        candle_of_force.to_excel(writer, sheet_name="Candle of Force")
        upper_shadow.to_excel(writer, sheet_name="Upper Shadows")
        lower_shadow.to_excel(writer, sheet_name="Lower Shadows")
        rsi14.to_excel(writer, sheet_name="RSI 14")


def moving_average(data, length, ma_type):
    supported_types = ["SMA", "EMA"]

    if ma_type.upper() not in supported_types:
        print(f"Supported MA types: {supported_types}")
        return None

    if length <= 1:
        print("parameter length must be more or equal to 2")
        return None

    print(f"Calculating {length} {ma_type} moving average......")
    df = pd.DataFrame()

    if ma_type == "SMA":
        df = data.rolling(window=length).mean()
    elif ma_type == "EMA":
        df = data.ewm(span=length, adjust=False).mean()

    print("Done!")
    return df.reindex(index=df.index[::-1])


def price_action(closes, opens, highs, lows, pattern):
    pattern = pattern.lower()
    supported_patterns = [
        "inside bar",
        "outside bar",
        "candle of force",
        "upper shadow",
        "lower shadow",
    ]

    if pattern not in supported_patterns:
        print(f"Supported Patterns: {supported_patterns}")
        return None

    print(f"Calculating {pattern}s......")

    df = pd.DataFrame()

    if pattern == "inside bar":
        df = (highs < highs.shift()) & (lows > lows.shift())
    elif pattern == "outside bar":
        df = (highs > highs.shift()) & (lows < lows.shift())
    elif pattern == "candle of force":
        df = (closes - opens).abs() / (highs - lows) > 0.75
    elif pattern == "upper shadow":
        df = ((closes >= opens) & (closes - lows <= 0.3 * (highs - lows))) | (
            (closes < opens) & (opens - lows <= 0.3 * (highs - lows))
        )
    elif pattern == "lower shadow":
        df = ((closes >= opens) & (highs - opens <= 0.3 * (highs - lows))) | (
            (closes < opens) & (highs - closes <= 0.3 * (highs - lows))
        )

    print("Done!")
    return df.reindex(index=df.index[::-1])


def rsi(data, length):
    delta_rsi = data.copy().diff(1)

    if length <= 1:
        print("parameter length must be more or equal to 2")
        return None

    print("Calculating RSIs......")

    df = pd.DataFrame()

    positive_rsi = delta_rsi.copy()
    positive_rsi[positive_rsi < 0] = 0
    positive_rsi.fillna(0, inplace=True)
    avg_gain_rsi = positive_rsi.rolling(window=length).mean()
    for row in range(length, len(avg_gain_rsi)):
        avg_gain_rsi.iloc[row] = (
            avg_gain_rsi.iloc[row - 1] * (length - 1) + positive_rsi.iloc[row]
        ) / length

    negative_rsi = delta_rsi.copy()
    negative_rsi[negative_rsi > 0] = 0
    negative_rsi.fillna(0, inplace=True)
    avg_loss_rsi = negative_rsi.abs().rolling(window=length).mean()
    for row in range(length, len(avg_gain_rsi)):
        avg_loss_rsi.iloc[row] = (
            avg_loss_rsi.iloc[row - 1] * (length - 1) - negative_rsi.iloc[row]
        ) / length

    df = 100 - (100 / (1 + (avg_gain_rsi / avg_loss_rsi)))

    print("Done!")
    return df.reindex(index=df.index[::-1])


if __name__ == "__main__":
    main()
