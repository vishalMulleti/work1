import json
import random
import urllib.request
import time

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# Number of server requests
N = 500


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
        return float('inf')  # Return infinity to indicate division by zero
    return price_a / price_b


# Main
if __name__ == "__main__":
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Ensure there are at least two stocks to calculate a ratio
        if len(prices) >= 2:
            stock_list = list(prices.keys())
            for i in range(len(stock_list)):
                for j in range(i + 1, len(stock_list)):
                    stock_a = stock_list[i]
                    stock_b = stock_list[j]
                    ratio = getRatio(prices[stock_a], prices[stock_b])
                    print("Ratio of %s to %s: %s" % (stock_a, stock_b, ratio))

        # Sleep for a while to avoid making requests too quickly
        time.sleep(1)
