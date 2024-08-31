def getRatio(price_a, price_b):
    # Handle division by zero
    if price_b == 0:
        return float('inf') 
    
    return price_a / price_b
