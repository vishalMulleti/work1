import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/stocks?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # Correct calculation for the average price
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get ratio of price_a and price_b"""
    # Check if price_b is zero to avoid division by zero
    if price_b == 0:
        return "Undefined (division by zero)"
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Dictionary to store stock prices
    prices = {}

    # Query the price once every N seconds.
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Dictionary to store datapoints for each stock
        datapoints = {}

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

            # Store the datapoint for the stock
            datapoints[stock] = (bid_price, ask_price, price)

        # Print the ratios for each stock
        for stock in datapoints:
            bid_price, ask_price, price = datapoints[stock]
            ratio = getRatio(price, ask_price)  # Calculate the ratio for each stock
            print("Ratio for %s: %s" % (stock, ratio))
