def getDataPoint(stock):   
    bid_price = get_bid_price(stock)  
    ask_price = get_ask_price(stock)  
    
    # Compute the stock price
    price = (bid_price + ask_price) / 2
    
    # Return the data point (price, bid_price, ask_price)
    return price, bid_price, ask_price
