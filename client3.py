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


def getDataPoint(stock):
    """ Produce all of the needed values to generate a datapoint """
    stock_name, bid_price, ask_price = stock['name'], float(stock['bid_price']), float(stock['ask_price'])
    price = (bid_price + ask_price) / 2
    return stock_name, bid_price, ask_price, price



def getRatio(price_a, price_b):
    """ Get ratio of price_a to price_b """
    if price_b == 0:
        return None
    return price_a / price_b


def main():
    query = json.loads(urllib.request.urlopen("http://localhost:8080/query").read())
    
    prices = {}
    
    for stock in query:
        stock_name, bid_price, ask_price, price = getDataPoint(stock)
        prices[stock_name] = price
        print(f"Quoted {stock_name} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

    price_a = prices.get("A")
    price_b = prices.get("B")
    
    if price_a is not None and price_b is not None:
        ratio = getRatio(price_a, price_b)
        print(f"Ratio {ratio}")
