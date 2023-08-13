import json
import random
import urllib.request
import time

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

# Dictionary to store stock prices
stock_prices = {}

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            stock_prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        if 'stock_a' in stock_prices and 'stock_b' in stock_prices:
            ratio = getRatio(stock_prices['stock_a'], stock_prices['stock_b'])
            print("Ratio %s" % ratio)

        time.sleep(1)  # Wait for 1 second before the next query
