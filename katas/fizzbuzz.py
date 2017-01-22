from future.utils import lmap

def fizzbuzz(input):
    multiples_3 = lmap(lambda x: (x % 3 == 0 and "Fizz") or x, input)

    return multiples_3
