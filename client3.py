

import json
import random

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = bid_price
    price = (bid_price + ask_price)/2

 
def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
if (price_b==0):
        return
return price_a/price_b

price={}
print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))


print("Ratio %s" %getRatio(price,price))
price("Ratio %s" %getRatio(price['ABC'],price['DEF']))
