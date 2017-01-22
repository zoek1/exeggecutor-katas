from unittest import TestCase
from katas.fizzbuzz import fizzbuzz

class TestFizzBuzz(TestCase):
  def test_if_fizz_is_substituted_instead_of_multiples_of_three(self):
      multiples = [3, 6, 9, 12]
      fizz_list = ['Fizz'] * len(multiples) 
      self.assertEqual(fizzbuzz(multiples), fizz_list, "All multiples of three must be subtituted by 'Fizz'")
