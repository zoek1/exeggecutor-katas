import unittest
from katas.rsa import get_factors, fast_get_factors

class GenerateBase(unittest.TestCase):
    def test_get_factors_of_any_mutiplication_of_primes_given_the_product(self):
        prime_products = [
            (6, [2, 3]),
            (15, [3, 5]),
            (35, [5, 7]),
            # (8633, [89,97]), # no descomentar o traera 10 min de mala suerte
            #(25282799, [8893, 2843]) # estas bromeando cierto?
        ]

        for (product, factors) in prime_products:
            self.assertEqual(get_factors(product), sorted(factors))

    def test_empty_array_if_number_is_not_product_of_two_primes(self):
        prime_no_products = [
            12,
            28,
            27
        ]

        for t in prime_no_products:
            self.assertEqual(get_factors(t), [])


class GenerateFastFactors(unittest.TestCase):
    def test_get_factors_of_any_mutiplication_of_primes_given_the_product(self):
        prime_products = [
            (6, [2, 3]),
            (15, [3, 5]),
            (35, [5, 7]),
            (8633, [89,97]),
            (25282799, [8893, 2843])
        ]

        for (product, factors) in prime_products:
            self.assertEqual(fast_get_factors(product), sorted(factors))

    def test_empty_array_if_number_is_not_product_of_two_primes(self):
        prime_no_products = [n * 3 * 7 for n in range(2, 10000)]

        for t in prime_no_products:
            val = fast_get_factors(t)

            self.assertEqual(val, [])
