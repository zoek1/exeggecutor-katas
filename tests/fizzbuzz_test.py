import unittest
from katas.fizzbuzz import fizz, buzz


def multiples(base, limit=100):
    """the most simple generator of multiples"""
    if limit < 0:
        return []

    if base == 0:
        return [0]

    return [base * limit for step in range(1, limit)]


def no_multiples(base, limit=100):
    """the most simple generator of non multiples"""
    no_multiples = []

    if base in [1, -1] or limit < 1:
        return []

    if base == 0:
        return list(range(1, limit))

    while len(no_multiples) < limit:
        no_multiples = [(base * len(no_multiples)) - 1] + no_multiples

    return no_multiples


class TestFizz(unittest.TestCase):
  def test_if_fizz_is_substituted_instead_of_multiples_of_three(self):
      multiples_list = multiples(3, 100)
      fizz_list = ['Fizz'] * len(multiples_list)
      self.assertEqual(fizz(multiples_list), fizz_list, "All multiples of three must be subtituted by 'Fizz'")

  def test_non_multiples_of_three_remains_equals(self):
      non_multiples_list = no_multiples(3, 100)
      self.assertEqual(fizz(non_multiples_list), non_multiples_list, "Non multiples of three must remains equals")


class TestBuzz(unittest.TestCase):
  def test_if_Buzz_is_substituted_instead_of_multiples_of_five(self):
      multiples_list = multiples(5, 100)
      fizz_list = ['Buzz'] * len(multiples_list)
      self.assertEqual(buzz(multiples_list), fizz_list, "All multiples of three must be subtituted by 'Fizz'")

  def test_non_multiples_of_five_remains_equals(self):
      non_multiples_list = no_multiples(5, 100)
      self.assertEqual(buzz(non_multiples_list), non_multiples_list, "Non multiples of three must remains equals")

