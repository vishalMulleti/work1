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
      self.assertEqual(getDataPoint(quote), {quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], quote['top_ask']['price'], quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), {quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], quote['top_ask']['price'], quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
      quotes = [
      {'top_ask': {'price': 101.13, 'size': 11}, 'timestamp': '2023-02-10 22:06:30.572453', 'top_bid': {'price': 135.10, 'size': 10}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 100.95, 'size': 426}, 'timestamp': '2020-10-10 22:06:30.572453', 'top_bid': {'price': 145.78, 'size': 225}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

""" getRatio Tests"""

    def test_getRatio(self):
        price_a = 101.12
        price_b = 135.75
        result = getRatio(price_a, price_b)
        expected_result = price_a / price_b
        self.assertEqual(result, expected_result)


        price_a = 111.11
        price_b = 0
        with self.assertRaises(ZeroDivisionError):
            getRatio(price_a, price_b)

        price_a = 0
        price_b = 134.32
        with self.assertRaises(ZeroDivisionError):
            getRatio(price_a, price_b)


if __name__ == '__main__':
    unittest.main()
