import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Corrected calculation
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    return price_a / price_b if price_b != 0 else float('inf')


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    prices = {}  # Dictionary to store prices of stocks
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store price in the dictionary
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        if len(prices) == 2:  # Ensure we have prices for both stocks
            stock_a, price_a = list(prices.items())[0]
            stock_b, price_b = list(prices.items())[1]
            ratio = getRatio(price_a, price_b)
            print("Ratio of %s to %s is %s" % (stock_a, stock_b, ratio))
