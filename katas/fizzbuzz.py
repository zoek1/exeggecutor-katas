from future.utils import lmap

def fizz(input):
    return lmap(lambda x: (x % 3 == 0 and "Fizz") or x, input)


def buzz(input):
    return lmap(lambda x: (x % 5 == 0 and "Buzz") or x, input)

def fizzbuzz(input):
    join = lambda f, b: (
        (f == 'Fizz' and b == 'Buzz' and "FizzBuzz") or
        (f == 'Fizz' and f) or # return Fizz only if fizz == 'Fizz'
        (b == 'Buzz' and b) or # return Buzz only if buzz == 'Buzz'
        f                      # return number if none of the above
    )

    return [join(f, b) for (f, b) in zip(fizz(input), buzz(input))]


def minify_fizzbuzz(input, fizz=3, buzz=5):
    fizzbuzz = fizz * buzz
    return [(
        ((x % fizzbuzz == 0) and "FizzBuzz") or
        ((x % fizz == 0) and "Fizz") or
        ((x % buzz == 0) and "Buzz") or
        x
    ) for x in input]
