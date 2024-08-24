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
        for i in quotes:
            expected_price = (i['top_bid']['price'] + i['top_ask']['price']) / 2
            self.assertEqual(getDataPoint(i),
                             (i['stock'], i['top_bid']['price'], i['top_ask']['price'], expected_price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for i in quotes:
            expected_price = (i['top_bid']['price'] + i['top_ask']['price']) / 2
            self.assertEqual(getDataPoint(i),
                             (i['stock'], i['top_bid']['price'], i['top_ask']['price'], expected_price))

    def test_getRatio_calculateCorrectly(self):
        # Test for correct ratio calculation
        price_a = 120.48
        price_b = 119.2
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, 120.48 / 119.2)

    def test_getRatio_priceBZero(self):
        # Test when price_b is 0 to avoid division by zero
        price_a = 120.48
        price_b = 0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)  # Assuming getRatio should return None if price_b is zero


if __name__ == '__main__':
    unittest.main()
