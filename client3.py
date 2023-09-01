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
    price = (bid_price + ask_price) / 2  # Calculate the average price
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None  # To avoid division by zero
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Initialize variables to keep track of prices
    price_a = 0
    price_b = 0

    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Loop through the quotes to update prices and calculate ratios
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            
            # Update price_a and price_b based on your requirements
            if stock == 'stock_a':
                price_a = price
            elif stock == 'stock_b':
                price_b = price

        ratio = getRatio(price_a, price_b)
        print("Ratio %s" % ratio)
