import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    # Ensure required fields are present
    if 'stock' not in quote or 'top_ask' not in quote or 'top_bid' not in quote:
        raise ValueError("Missing required fields in the quote")

    stock = quote['stock']
    top_bid_price = quote['top_bid']['price']
    top_ask_price = quote['top_ask']['price']

    # Check for invalid or zero prices
    try:
        bid_price = float(top_bid_price)
        ask_price = float(top_ask_price)
    except (TypeError, ValueError):
        raise ValueError("Invalid price data in quote")

    if bid_price <= 0 or ask_price <= 0:
        raise ValueError("Prices must be greater than zero")

    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price



def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        raise ZeroDivisionError("price_b cannot be zero")
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Assuming both ABC and DEF stocks exist in the response
        try:
            print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
        except ZeroDivisionError as e:
            print("Error:", e)
