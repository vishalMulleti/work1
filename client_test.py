import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_normal_case(self):
        quote = {
            'top_ask': {'price': 121.2, 'size': 36},
            'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109},
            'id': '0.109974697771',
            'stock': 'ABC'
        }

        expected_data_point = (
            'ABC',
            120.48,
            121.2,
            (120.48 + 121.2) / 2  # Calculate price based on formula
        )
        data_point = getDataPoint(quote)

        self.assertEqual(data_point, expected_data_point)

    def test_getDataPoint_bid_greater_than_ask(self):
        quote = {
            'top_ask': {'price': 119.2, 'size': 36},
            'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109},
            'id': '0.109974697771',
            'stock': 'ABC'
        }

        expected_data_point = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
        data_point = getDataPoint(quote)

        self.assertEqual(data_point, expected_data_point)

    def test_getDataPoint_empty_quote(self):
        quote = {'stock': 'XYZ', 'top_ask': {'price': 100.0}, 'top_bid': {'price': 0.0}}

        with self.assertRaises(ValueError):
            getDataPoint(quote)

    def test_getDataPoint_missing_fields(self):
        quote = {
            'top_ask': {'price': 121.2, 'size': 36},
            'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109}
        }  # Missing 'id' and 'stock' fields

        with self.assertRaises(ValueError):
            getDataPoint(quote)

    def test_getDataPoint_invalid_prices(self):
        quote = {
            'top_ask': {'price': 'invalid', 'size': 36},
            'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109},
            'id': '0.109974697771',
            'stock': 'ABC'
        }

        with self.assertRaises(ValueError):
            getDataPoint(quote)

    # Assuming getRatio exists in client3.py
    def test_getRatio_normal_case(self):
        price_a = 100
        price_b = 120
        expected_ratio = price_a / price_b

        ratio = getRatio(price_a, price_b)

        self.assertEqual(ratio, expected_ratio)

    def test_getRatio_price_b_zero(self):
        price_a = 100
        price_b = 0

        with self.assertRaises(ZeroDivisionError):
            getRatio(price_a, price_b)

    def test_getRatio_price_a_zero(self):
        price_a = 0
        price_b = 120

        ratio = getRatio(price_a, price_b)

        self.assertEqual(ratio, 0)

if __name__ == '__main__':
    unittest.main()