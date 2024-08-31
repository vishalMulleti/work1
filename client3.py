import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# Number of server requests
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate the average of bid and ask prices
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None  # Avoid division by zero
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        try:
            # Fetch the stock data from the server
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        except Exception as e:
            print(f"Error fetching data: {e}")
            continue

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Calculate the ratio between the first two stocks (if at least two stocks are available)
        if len(prices) >= 2:
            stock_a, stock_b = list(prices.keys())[:2]  # Get the first two stocks
            ratio = getRatio(prices[stock_a], prices[stock_b])
            if ratio is not None:
                print("Ratio of %s to %s is %s" % (stock_a, stock_b, ratio))
            else:
                print(f"Ratio of {stock_a} to {stock_b} is undefined (division by zero).")
