from functools import wraps
import math

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
    step = 0
    number = primes[1]
    while step != index:
        number += 1
        prime = True
        for s in range(1, step // 2, 2):
            if (number // search_prime(s)) == 0:
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
        print("roof", index)


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
