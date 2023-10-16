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
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_A, price_B):
    """ Get ratio of price_A and price_B """
    if price_B == 0:
        return "undefined (Division by Zero)"
    ratio = price_A / price_B
    return ratio


# Main
if __name__ == "__main":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        ratio_sum = 0
        ratio_count = 0

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            ratio_sum += price

        if ratio_count > 0:
            average_price = ratio_sum / ratio_count
            ratio = getRatio(price, average_price)
            print("Price Ratio: %s" % ratio)
