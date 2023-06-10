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
import matplotlib.pyplot as plt

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500
# change 1
# Stocks to monitor
stock_a = "AAPL"
stock_b = "MSFT"

# Historical prices
prices_a = []
prices_b = []
ratios = []
# chanege 1 end

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
# change 2
    price = (bid_price + ask_price) / 2
# change 2 end
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
# change 3
    ratio = price_a / price_b
# change 3 end    
    return ratio

# change 4 
def plotData(prices_a, prices_b):
    """ Plot the data """
    plt.title("Stock prices over time")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.plot(prices_a)
    plt.plot(prices_b)
    plt.legend([stock_a, stock_b])
    plt.show()


def plotRatio(ratios):
    """ Plot the ratio """
    plt.title("Stock price ratio over time")
    plt.xlabel("Time")
    plt.ylabel("Ratio")
    plt.plot(ratios)
    plt.show()
# change 4 end

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
# change 5
            if stock == stock_a:
                prices_a.append(price)
            elif stock == stock_b:
                prices_b.append(price)

        # Calculate the ratio of the two stock prices
        if len(prices_a) > 0 and len(prices_b) > 0:
            ratio = getRatio(prices_a[-1], prices_b[-1])
            ratios.append(ratio)

            # Visualize the historical correlation between the two stocks
            if len(ratios) > 1:
                ratio_change = ratios[-1] / ratios[-2] - 1
                if abs(ratio_change) > 0.05:
                    print("Correlation weakened: %s" % ratio_change)
                    plotData(prices_a, prices_b)
                    plotRatio(ratios)
# change 5 end