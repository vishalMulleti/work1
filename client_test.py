def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = quote['top_bid']['price']
    ask_price = quote['top_ask']['price']
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price
