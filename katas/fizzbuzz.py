from future.utils import lmap

def fizz(input):
    return lmap(lambda x: (x % 3 == 0 and "Fizz") or x, input) 


def fizzbuzz(input):
    pass
