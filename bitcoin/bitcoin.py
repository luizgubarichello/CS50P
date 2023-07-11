import requests
import sys

cline = sys.argv

try:
    cline = sys.argv
    bitcoin_qty = float(cline[1])
    bitcoin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin_price = float(bitcoin_info["bpi"]["USD"]["rate"].strip().replace(",",""))
    print(f"${(bitcoin_qty*bitcoin_price):,.4f}")
except requests.RequestException:
    sys.exit("Request not successful")
except (ValueError, IndexError):
    sys.exit("Invalid input")