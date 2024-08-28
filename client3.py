import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # Compute the price as the average of bid and ask
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    # Handle division by zero
    if price_b == 0:
        return float('inf')  # or handle as needed
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the latest price for each stock
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Compute and print ratios if there are at least two stocks
        if len(prices) >= 2:
            stock_list = list(prices.keys())
            price_a = prices[stock_list[0]]
            price_b = prices[stock_list[1]]
            ratio = getRatio(price_a, price_b)
            print("Ratio %s" % ratio)
        else:
            print("Not enough stocks to calculate ratio")
