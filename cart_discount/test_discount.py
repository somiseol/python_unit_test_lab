import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_prices(self):
        prices = [10, 4, 20, 2]
        expected_discount = 2
        self.assertEqual(expected_discount, discount(prices))

    def test_two(self):
        prices = [2, 5]
        self.assertEqual(0, discount(prices))

    def test_one(self):
        prices = [2]
        self.assertEqual(0, discount(prices))

    def test_negative_prices(self):
        with self.assertRaises(NegativePriceException): # custom error
            discount([10, 5, -1])

    def test_empty_list(self):
        self.fail('TODO empty list')

    def test_type_error(self):
        with self.assertRaises(TypeError):
            discount("cat")

    def test_dictionary_instead_of_list(self):
        self.fail('TODO dictionary instead of list')

    def test_missing_price(self):
        prices = [1, 4, None, 2]
        self.fail('TODO None price')

    def test_float_prices(self):
        self.fail('TODO float prices')

    def test_duplicate_prices(self):
        self.fail('TODO duplicate prices')

    def test_all_same_prices(self):
        self.fail('TODO all same prices')


if __name__ == '__main__':
    unittest.main()
