from unittest import TestCase
from katas.fizzbuzz import fizzbuzz

class TestFizzBuzz(TestCase):
  def test_if_fizz_is_substituted_instead_of_multiples_of_three(self):
      multiples = [3, 6, 9, 12]
      fizz_list = ['Fizz'] * len(multiples) 
      self.assertEqual(fizzbuzz(multiples), fizz_list, "All multiples of three must be subtituted by 'Fizz'")

  def test_non_multiples_of_three_remains_equals(self):
      non_multiples = [5, 7, 8, 11, 17, 13, 19]
      self.assertEqual(fizzbuzz(non_multiples), non_multiples, "Non multiples of three must remains equals")
