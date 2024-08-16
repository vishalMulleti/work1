import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_withZeroBidPrice(self):
    quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        # Assertions
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 0.0, 121.2, (0.0 + 121.2) / 2))

  def test_getDataPoint_withZeroAskPrice(self):
    quotes = [
            {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        # Assertions
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 0.0, (120.48 + 0.0) / 2))


if __name__ == '__main__':
    unittest.main()
