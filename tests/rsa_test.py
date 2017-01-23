import unittest
import random
import fractions
from katas.rsa import (get_factors,
                       fast_get_factors,
                       phi,
                       coprime,
                       search_prime,
                       public_key,
                       private_key,
                       keygen,
                       cipher,
                       decipher)

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


class PrivateAndPublicKeys(unittest.TestCase):
    def test_phi_as_product_of_factor1_minus_one_and_factor2_two_minus_one(self):
        prime_products = [
            (2, [2, 3]),
            (8, [3, 5]),
            (24, [5, 7]),
            (8448, [89,97]),
            (25271064, [8893, 2843])
        ]

        for (result, factors) in prime_products:
            self.assertEqual(phi(factors[0] * factors[1]), result)


    def test_coprime_of_given_number(self):
        prime_products = [ 15, 35, 8633]

        for prime_product in prime_products:
            t = phi(prime_product)
            c = coprime(prime_product)
            self.assertEqual(fractions.gcd(prime_product, t), 1)


    def test_public_key_is_coprime_between_e_and_n(self):
        random.seed()
        for e in range(1, 100):
            p = search_prime(random.randint(5, 20))
            q = search_prime(random.randint(8, 20))

            n = p * q
            t = phi(n)
            pk = public_key(n)

            self.assertEqual(fractions.gcd(pk[0], t), 1)
            self.assertEqual(pk[1], n)


    def test_public_key_is_coprime_between_e_and_n(self):
        random.seed()
        for e in range(1, 10):
            p = search_prime(random.randint(3, 8))
            q = search_prime(random.randint(3, 8))

            n = p * q
            t = phi(n)
            pk = public_key(n)
            ik = private_key(pk)

            self.assertEqual(pk[1], ik[1])
            self.assertEqual(pk[1], n)
            self.assertEqual((pk[0] * ik[0]) % t, 1)


    def test_cypher_and_decypher_message(self):
        msg = 'Hello World!'
        (public, private) = keygen()
        self.assertEqual(decipher(private, cipher(public, msg)), msg)
