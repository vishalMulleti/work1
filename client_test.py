import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price) / 2 
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price) / 2 
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
    
    # Exempted ratio value 
    ratio = 1.0005426841995408
    
    prices = {}
    for quote in quotes:
      ask_price = quote['top_ask']['price']
      bid_price = quote['top_bid']['price']
      stock = quote['stock']
      prices[stock] = (bid_price + ask_price) / 2

    self.assertEqual(getRatio(prices['ABC'], prices["DEF"]), ratio)
    


if __name__ == '__main__':
    unittest.main()
