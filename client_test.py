import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price)/2
      expected = stock, bid_price, ask_price, price
      actual = getDataPoint(quote)
      self.assertEqual(expected, actual)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      #for the 2nd quote, the original bid price (117.87) wasn't greater than the original ask price (121.68) so I swapped them
      {'top_ask': {'price': 117.87, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price)/2
      expected = stock, bid_price, ask_price, price
      actual = getDataPoint(quote)
      self.assertEqual(expected, actual)


  """ ------------ Add more unit tests ------------ """
  #price_a is positive and price_b = 0
  def test_getRatio_calculateZeroPriceB(self):
    price_a = 1
    price_b = 0
    ratio = getRatio(price_a, price_b)
    self.assertIsNone(ratio)


  #price_a = 0 and price_b is positive
  def test_getRatio_calculateZeroPriceA(self):
    price_a = 0
    price_b = 1
    expected = price_a / price_b
    actual = getRatio(price_a, price_b)
    self.assertEqual(expected, actual)


  #price_a > price_b and price_b is positive
  def test_getRatio_calculatePriceAGreaterThanNonZeroPriceB(self):
    price_a = 6
    price_b = 2
    expected = price_a / price_b
    actual = getRatio(price_a, price_b)
    self.assertEqual(expected, actual)


  #price_b > price_a and price_a is positive
  def test_getRatio_calculatePriceBGreaterThanNonZeroPriceA(self):
    price_a = 1
    price_b = 3
    expected = price_a / price_b
    actual = getRatio(price_a, price_b)
    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
