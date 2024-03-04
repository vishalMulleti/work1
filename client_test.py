import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Assume getDataPoint returns a tuple like (stock, bid_price, ask_price, price)
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(price, (quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
  # Assume getDataPoint returns a tuple like (stock, bid_price, ask_price, price)
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint(self):
    quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    stock, bid_price, ask_price, price = getDataPoint(quote)
    self.assertEqual(stock, 'ABC')
    self.assertEqual(bid_price, 120.48)
    self.assertEqual(ask_price, 121.2)
    self.assertEqual(price, (120.48 + 121.2) / 2)

  def test_getRatio_priceB_zero(self):
    self.assertIsNone(getRatio(1, 0))

  def test_getRatio_priceA_zero(self):
    self.assertEqual(getRatio(0, 1), 0)

  def test_getRatio_greater_than_1(self):
    self.assertGreater(getRatio(1, 0.5), 1)

  def test_getRatio_less_than_1(self):
    self.assertLess(getRatio(0.5, 1), 1)

  def test_getRatio_exactly_one(self):
    self.assertEqual(getRatio(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
