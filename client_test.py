import unittest
from client3 import getDataPoint  # Assuming client3 contains the implementation of getDataPoint

class TestDataPoint(unittest.TestCase):
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        result = getDataPoint(quotes)
        self.assertEqual(result, (119.2, 120.48, (119.2 + 120.48) / 2))

    def test_getDataPoint_noQuotes(self):
        quotes = []
        result = getDataPoint(quotes)
        self.assertIsNone(result)

    def test_getDataPoint_singleQuote(self):
        quotes = [{'top_ask': {'price': 100, 'size': 10}, 'top_bid': {'price': 95, 'size': 15}}]
        result = getDataPoint(quotes)
        self.assertEqual(result, (100, 95, (100 + 95) / 2))

    def test_getDataPoint_multipleQuotes(self):
        quotes = [
            {'top_ask': {'price': 110, 'size': 20}, 'top_bid': {'price': 105, 'size': 25}},
            {'top_ask': {'price': 112, 'size': 22}, 'top_bid': {'price': 106, 'size': 28}},
            {'top_ask': {'price': 108, 'size': 18}, 'top_bid': {'price': 103, 'size': 23}}
        ]
        result = getDataPoint(quotes)
        self.assertEqual(result, (110, 106, (110 + 106) / 2))

if __name__ == '__main__':
    unittest.main()
