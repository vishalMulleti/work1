import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call getDataPoint for the first quote and extract the stock price
        data_point_1 = getDataPoint(quotes[0]['stock'], quotes[0]['top_bid']['price'], quotes[0]['top_ask']['price'])
        # Assert the calculated price is equal to the expected price
        self.assertEqual(data_point_1['price'], (quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2)

        # Call getDataPoint for the second quote and extract the stock price
        data_point_2 = getDataPoint(quotes[1]['stock'], quotes[1]['top_bid']['price'], quotes[1]['top_ask']['price'])
        # Assert the calculated price is equal to the expected price
        self.assertEqual(data_point_2['price'], (quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price']) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call getDataPoint for the first quote and extract the stock price
        data_point_1 = getDataPoint(quotes[0]['stock'], quotes[0]['top_bid']['price'], quotes[0]['top_ask']['price'])
        # Assert the calculated price is equal to the expected price
        self.assertEqual(data_point_1['price'], (quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2)

        # Call getDataPoint for the second quote and extract the stock price
        data_point_2 = getDataPoint(quotes[1]['stock'], quotes[1]['top_bid']['price'], quotes[1]['top_ask']['price'])
        # Assert the calculated price is equal to the expected price
        self.assertEqual(data_point_2['price'], (quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price']) / 2)


if __name__ == '__main__':
    unittest.main()
