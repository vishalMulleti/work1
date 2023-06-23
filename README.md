# JPMC Task 1
Starter repo for task 1 of the JPMC software engineering program
def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    """Produce all the needed values to generate a datapoint"""
    """------------- Update this function -------------"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = bid_price
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price



def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    return 1
    """Get ratio of price_a and price_b"""
    """------------- Update this function -------------"""
    if price_b == 0:
        return None  # or any value that represents the division by zero scenario
    ratio = price_a / price_b
    return ratio



# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    prices = {}  # Dictionary to store stock prices

    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        """----------- Update to get the ratio ---------------"""
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the price in the prices dictionary
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        print("Ratio %s" % getRatio(price, price))
        # Calculate and print the ratio
        if len(prices) >= 2:  # Ensure at least two stock prices are available
            stock_names = list(prices.keys())
            price_a = prices[stock_names[0]]
            price_b = prices[stock_names[1]]
            ratio = getRatio(price_a, price_b)
            print("Ratio of %s to %s: %s" % (stock_names[0], stock_names[1], ratio))
        else:
            print("Not enough data points to calculate the ratio.")

