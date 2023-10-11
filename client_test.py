import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call the getDataPoint function with the first quote
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])

        # Add assertions to verify the correctness of the calculated price
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.2)
        self.assertEqual(price, bid_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Call the getDataPoint function with the second quote
        stock, bid_price, ask_price, price = getDataPoint(quotes[1])

        # Add assertions to verify the correctness of the calculated price
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 117.87)
        self.assertEqual(ask_price, 121.68)
        self.assertEqual(price, bid_price)

    
if __name__ == '__main__':
    unittest.main()
