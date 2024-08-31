import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(price, expected_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(price, expected_price)

    def test_getRatio_priceBZero(self):
        price_a = 120.48
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))  # Test for division by zero

    def test_getRatio_valid(self):
        price_a = 120.48
        price_b = 119.2
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)  # Test for valid ratio

    def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 121.2
        expected_ratio = 0
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)  # Test for price_a zero


if __name__ == '__main__':
    unittest.main()
