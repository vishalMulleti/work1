import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):

  # test for getDataPoint

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), 
                       (quote['stock'], 
                        quote['top_bid']['price'], 
                        quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
                      )

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), 
                       (quote['stock'], 
                        quote['top_bid']['price'], 
                        quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
                      )

  # Test for getRatio

  def test_getRatio_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}    
    ]
    # Extracting quotes for ABC and DEF
    quote_abc = next(quote for quote in quotes if quote['stock'] == 'ABC')
    quote_def = next(quote for quote in quotes if quote['stock'] == 'DEF')
    # Calculating prices for ABC and DEF
    price_a = (quote_abc['top_bid']['price'] + quote_abc['top_ask']['price']) / 2
    price_b = (quote_def['top_bid']['price'] + quote_def['top_ask']['price']) / 2
    self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

  def test_getRatio_calculateRatioPriceBEqualsZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}    
    ]
    # Extracting quotes for ABC and DEF
    quote_abc = next(quote for quote in quotes if quote['stock'] == 'ABC')
    quote_def = next(quote for quote in quotes if quote['stock'] == 'DEF')
    # Calculating prices for ABC and DEF
    price_a = (quote_abc['top_bid']['price'] + quote_abc['top_ask']['price']) / 2
    price_b = (quote_def['top_bid']['price'] + quote_def['top_ask']['price']) / 2
    self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
    unittest.main()
