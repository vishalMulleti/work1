import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, calculated_price = getDataPoint(quote)
            expected_stock, expected_bid, expected_ask, expected_calculated = expected_results[i]
            
            self.assertEqual(stock, expected_stock)
            self.assertEqual(bid_price, expected_bid)
            self.assertEqual(ask_price, expected_ask)
            self.assertEqual(calculated_price, expected_calculated)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, calculated_price = getDataPoint(quote)
            expected_stock, expected_bid, expected_ask, expected_calculated = expected_results[i]
            
            self.assertEqual(stock, expected_stock)
            self.assertEqual(bid_price, expected_bid)
            self.assertEqual(ask_price, expected_ask)
            self.assertEqual(calculated_price, expected_calculated)

    def test_getDataPoint_handleZeroAskPrice(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'XYZ'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'PQR'}
        ]
        
        expected_results = [
            ('XYZ', 120.48, 0, None),  # Handle division by zero scenario
            ('PQR', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, calculated_price = getDataPoint(quote)
            expected_stock, expected_bid, expected_ask, expected_calculated = expected_results[i]
            
            self.assertEqual(stock, expected_stock)
            self.assertEqual(bid_price, expected_bid)
            self.assertEqual(ask_price, expected_ask)
            self.assertEqual(calculated_price, expected_calculated)

if __name__ == '__main__':
    unittest.main()
