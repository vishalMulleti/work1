import unittest
from client3 import getDataPoint
from client3 import getRatio
class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()

class TestYourFunctions(unittest.TestCase):

  # Test when price_b = 0

  def test_divide_by_zero(self):
    price_a = 7
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

#Tests If price_a is equal to zero
def test_a_is_zero(self):
    price_a = 0
    price_b = 8
    self.assertIsEqual(getRatio(price_a, price_b),0)

#Tests for normal inputs
def normal_case(self):
  price_a = 200
  price_b = 10
  self.assertIsEqual(getRatio(price_a, price_b), 20)

#When neither variable are zero and price_a is a float
def float_case(self):
  price_a = 200.5
  price_b = 10
  self.assertIsEqual(getRatio(price_a, price_b), 20.05)

