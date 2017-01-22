import unittest
from katas.fizzbuzz import fizz, buzz


class TestFizz(unittest.TestCase):
  def test_if_fizz_is_substituted_instead_of_multiples_of_three(self):
      multiples = [3, 6, 9, 12]
      fizz_list = ['Fizz'] * len(multiples)
      self.assertEqual(fizz(multiples), fizz_list, "All multiples of three must be subtituted by 'Fizz'")

  def test_non_multiples_of_three_remains_equals(self):
      non_multiples = [7, 8, 11, 17, 13, 19]
      self.assertEqual(fizz(non_multiples), non_multiples, "Non multiples of three must remains equals")

class TestBuzz(unittest.TestCase):
  def test_if_Buzz_is_substituted_instead_of_multiples_of_five(self):
      multiples = [5, 10, 15, 20, 25, 30, 35]
      fizz_list = ['Buzz'] * len(multiples)
      self.assertEqual(buzz(multiples), fizz_list, "All multiples of three must be subtituted by 'Fizz'")

  def test_non_multiples_of_five_remains_equals(self):
      non_multiples = [3, 4, 7, 8, 9, 11, 17, 13, 19]
      self.assertEqual(buzz(non_multiples), non_multiples, "Non multiples of three must remains equals")

