import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_prices = [120.84, 119.775]
    for i, quote in enumerate(quotes):
        expected_price = expected_prices[i]
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertAlmostEqual(price, expected_price, places=2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_prices = [119.84, 119.775]  # Expected prices based on the given quotes
    for i, quote in enumerate(quotes):
        expected_price = expected_prices[i]
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertAlmostEqual(price, expected_price, places=2)

  def test_getDataPoint(self):
    # Test case: bid price and ask price are positive non-zero values
    quote1 = {
      "stock": "XYZ",
      "top_bid": {
        "price": "10.50",
        "volume": 100
      },
      "top_ask": {
        "price": "11.50",
        "volume": 200
      }
    }
    expected_result1 = ("XYZ", 10.50, 11.50, 11.0)
    self.assertEqual(getDataPoint(quote1), expected_result1)

    # Test case: bid price is zero
    quote2 = {
      "stock": "ABC",
      "top_bid": {
        "price": "0",
        "volume": 0
      },
      "top_ask": {
        "price": "5.50",
        "volume": 100
      }
    }
    expected_result2 = ("ABC", 0.0, 5.50, 2.75)
    self.assertEqual(getDataPoint(quote2), expected_result2)

    # Test case: ask price is zero
    quote3 = {
      "stock": "DEF",
      "top_bid": {
        "price": "10.50",
        "volume": 100
      },
      "top_ask": {
        "price": "0",
        "volume": 0
      }
    }
    expected_result3 = ("DEF", 10.50, 0.0, 5.25)  # Update the expected price to 5.25
    self.assertEqual(getDataPoint(quote3), expected_result3)

  def test_getRatio(self):
    self.assertEqual(getRatio(100.0, 50.0), 2.0)
    self.assertIsNone(getRatio(100.0, 0))
    self.assertEqual(getRatio(0, 100.0), 0.0)

  def test_getDataPoint(self):
    # Test case: bid price and ask price are positive non-zero values
    quote1 = {
      "stock": "XYZ",
      "top_bid": {
        "price": "10.50",
        "volume": 100
      },
      "top_ask": {
        "price": "11.50",
        "volume": 200
      }
    }
    expected_result1 = ("XYZ", 10.50, 11.50, 11.0)
    self.assertEqual(getDataPoint(quote1), expected_result1)

    # Test case: bid price is zero
    quote2 = {
      "stock": "ABC",
      "top_bid": {
        "price": "0",
        "volume": 0
      },
      "top_ask": {
        "price": "5.50",
        "volume": 100
      }
    }
    expected_result2 = ("ABC", 0.0, 5.50, 2.75)
    self.assertEqual(getDataPoint(quote2), expected_result2)

    # Test case: ask price is zero
    quote3 = {
      "stock": "DEF",
      "top_bid": {
        "price": "10.50",
        "volume": 100
      },
      "top_ask": {
        "price": "0",
        "volume": 0
      }
    }
    expected_result3 = ("DEF", 10.50, 0.0, 5.25)  # Update the expected price to 5.25
    self.assertEqual(getDataPoint(quote3), expected_result3)

  def test_getRatio(self):
    self.assertEqual(getRatio(100.0, 50.0), 2.0)
    self.assertIsNone(getRatio(100.0, 0))
    self.assertEqual(getRatio(0, 100.0), 0.0)


if __name__ == '__main__':
    unittest.main()
