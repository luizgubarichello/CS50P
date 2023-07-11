# TECHNICAL ANALYSIS INDICATORS FOR TRADING
#### Video Demo:  <https://youtu.be/ERg9-jfN2Vc>
#### Description: This prject outputs some TA indicators used for trading in an excel file.

## main()

    Returns an excel file with the specified TA indicators as sheets. Also returns closing, opening, highs, lows and volume for the inputted tickers.

### First input

    Expects the user to give the tickers used to calculate the indicators. Should be numeric equal to 1, 2 or 3.

    1 ->
    Will ask the user to reference an excel file. IT MUST HAVE A COLLUMN CALLED 'Ticker'. This collumn will be used to get all tickers below the header.

    2 ->
    Will ask the user to reference a csv file that contains the tickers. 

    3 ->
    The user will input all tickers it wants via terminal, one by one. Type 'Done!' when all tickers were given.

### Second input

    Expects the user to give an filename to output the excel file with the calculated values.

### Third input

    Expects the user to give how many days prior to the execution date will be downloaded to calculate the TA indicators.

### Output

    Outputs an excel file with the specified TA indicators as sheets. Also returns closing, opening, highs, lows and volume for the inputted tickers.

## moving_average(data, length, ma_type)

    Returns a pandas dataframe with the specified MA parameters used

    data ->
    pandas dataframe containing price data

    length ->
    length used to calculate the MA

    ma_type ->
    'SMA' for simple moving average
    'EMA' for exponential moving average

## price_action(closes, opens, highs, lows, pattern)

    Returns a pandas dataframe with True or False values representing if there is a pattern happening or not.

    closes ->
    pandas dataframe containing closing price data

    opens ->
    pandas dataframe containing opening price data

    highs ->
    pandas dataframe containing highs price data

    lows ->
    pandas dataframe containing lows price data

    pattern ->
    'inside bar' for inside bars
    'outside bar' for outside bars
    'candle of force' for strong candles
    'upper shadow' for big upper shadow cases
    'lower shadow' for big lower shadow cases

## rsi(data, length)

    Returns a pandas dataframe with the RSI values of the given parameters

    data ->
    pantas dataframe containing price data

    length ->
    length used to calculate the RSI