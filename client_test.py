import unittest
from client3 import getDataPoint, getRatio

global quotes
quotes = [
    {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
     'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
     'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
]


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            with self.subTest(quote=quote):
                self.assertEqual(getDataPoint(quote), (
                    quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            with self.subTest(quote=quote):
                self.assertEqual(getDataPoint(quote), (
                    quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio(self):
        """ ------------ Add the assertion below ------------ """
        prices = []
        for quote in quotes:
            prices.append((quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
        with self.subTest(quote=quote):
            self.assertEqual(round(getRatio(prices[0], prices[1]), 4), 1.0005)

    def test_getRatio_bis0(self):
        global quotes
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = []
        for quote in quotes:
            prices.append((quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
        with self.subTest(prices=prices):
            self.assertIsNone(getRatio(prices[0], prices[1]))


if __name__ == '__main__':
    unittest.main()
