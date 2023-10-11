################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

# variables to store the last prices of two stocks
last_price_a = None
last_price_b = None


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = bid_price
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b is not None and price_b != 0:
        return price_a / price_b
    return None


# Main
if __name__ == "__main":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            if stock == 'AAPL':
                price_a = price
            elif stock == 'MSFT':
                price_b = price

        # Check if we have both prices
        if price_a is not None and price_b is not None:
            price_ratio = getRatio(price_a, price_b)
            if price_ratio is not None:
                print("Quoted AAPL at (bid:%s, ask:%s, price:%s)" % (bid_price, ask_price, price_a))
                print("Quoted MSFT at (bid:%s, ask:%s, price:%s)" % (bid_price, ask_price, price_b))
                print("Ratio %s" % price_ratio)
        else:
            print("Missing price data for one or both stocks")

        last_price_a = price_a
        last_price_b = price_b