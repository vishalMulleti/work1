import unittest
import client3

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes=[
            {'top_ask':{'price':121.2, 'size':36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 128.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 171.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(client3.getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

    def test_getDataPoint_calculatePriceBidGraterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 171.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(client3.getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


    def test_getRatio_calculateRatioPriceAZero(self):
        price_A = 0
        price_B = 171.48
        self.assertEqual(0, client3.getRatio(price_A, price_B))

    def test_getRatio_calculateRatioPriceBZero(self):
        price_A = 171.48
        price_B = 0
        self.assertEqual(None, client3.getRatio(price_A, price_B))

    def test_getRatio_calculateRatioPrice(self):
        price_A = 121.68
        price_B = 109.2
        self.assertLess(0, client3.getRatio(price_A, price_B))
