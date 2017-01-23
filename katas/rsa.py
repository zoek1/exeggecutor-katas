from functools import wraps
import fractions
import math
import random


primes = list([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61])

def memoize(func):
    @wraps(func)
    def evaluation(index):
        list_index = index - 1
        result = 0

        if len(primes) > list_index:
            result = primes[list_index]

        if result == 0:
            prime = func(index)
            primes.append(prime)
            result = prime

        return result

    return evaluation


@memoize
def search_prime(index):
    step = len(primes)
    number = primes[-1]

    while step != index:
        number += 1
        prime = True
        for s in range(1, len(primes) - 1):
            if (number % search_prime(s)) == 0:
                prime = False
                break

        if prime:
            step += 1

    return number


def first_prime_before(roof):
    split_roof = roof // 2
    index = 1

    while search_prime(index) < split_roof:
        index += 1

    return (search_prime(index), index)


def get_factors(product):
    (p, multiplicand) = first_prime_before(product)
    multiplier = 1
    total = product - (search_prime(multiplicand) * search_prime(multiplier))

    while total != 0:
        if total < 0:
            multiplicand -= 1
        if total > 0:
            multiplier += 1

        if multiplicand < 2 or multiplier > (product // 2):
            return []

        total = product - (search_prime(multiplicand) * search_prime(multiplier))

    return sorted([search_prime(multiplicand), search_prime(multiplier)])


def simple_test_prime(number):
    if (number == 2):
        return True

    if (number % 2 == 0):
        return False

    for i in range(3, number // 2, 2):
        if number != i and number % i == 0:
            return False

    return True


def fast_get_factors(roof):
    factors = []

    if roof % 2 == 0:
        if simple_test_prime(roof // 2):
            return sorted([2, roof // 2])
        else:
            return []

    for step in range(3, roof // 2, 2):
        if roof % step == 0:
            if simple_test_prime(step) and simple_test_prime(roof // step):
                return sorted([step, roof // step])

    return []


def phi(n):
    (p, q) = fast_get_factors(n)
    return (p-1) * (q-1)


def coprimes(limit):
    coprimes = []
    p = phi(limit)
    for e in range(2, p):
        if fractions.gcd(e, p) == 1:
            coprimes = [e] + coprimes

    return coprimes


def coprime(limit):
    random.seed()
    coprimes_list = coprimes(limit)
    if len(coprimes_list) > 1:
        return coprimes_list[random.randint(1, len(coprimes_list)) - 1]

    return coprimes_list[0]


def public_key(limit):
    return (coprime(limit), limit)


def private_key(public_key):
    step = 1
    p = phi(public_key[1])

    while (step * public_key[0]) % p != 1:
        print(step, public_key[0], (step * public_key[0]) % p, 1)
        step += 1

    return (step, public_key[1])


def generate_base(index, index2):
    return search_prime(index) * search_prime(index2)


def keygen(base1=random.randint(3, 8), base2=random.randint(3, 8)):
    p = search_prime(base1)
    q = search_prime(base2)

    product = p * q

    publick = public_key(product)
    privatek = private_key(publick)

    return publick, privatek


def cipher(publick, msg):
    return [(ord(x) ** publick[0]) % publick[1] for x in msg]


def decipher(private, msg):
    b = [chr((x ** private[0]) % private[1]) for x in msg]
    return "".join(b)
