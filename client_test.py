import unittest
from client3 import getDataPoint, getRatio

class TestClient3(unittest.TestCase):

    def test_getDataPoint(self):
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': 120.48},
            'top_ask': {'price': 121.22}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.22)
        self.assertEqual(price, (120.48 + 121.22) / 2)

    def test_getRatio(self):
        self.assertEqual(getRatio(120.48, 121.22), 120.48 / 121.22)
        self.assertEqual(getRatio(120.48, 0), None)
        self.assertEqual(getRatio(0, 121.22), 0)

if __name__ == '__main__':
    unittest.main()