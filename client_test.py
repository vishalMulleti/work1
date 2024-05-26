import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

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

    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price) / 2
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))


  def test_getRatio(self):
    # (price_a, price_b)
    price_pairs = [
      (119.2, 121.68),
      (0, 14.56),
      (14.56, 0),
      (132, 145),
    ]

    for pair in price_pairs:
      price_a = pair[0]
      price_b = pair[1]
      ratio = price_a / price_b if price_b > 0 else None
      self.assertEqual(getRatio(price_a, price_b), ratio)



if __name__ == '__main__':
    unittest.main()
