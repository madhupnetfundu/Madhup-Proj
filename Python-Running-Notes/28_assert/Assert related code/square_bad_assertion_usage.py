# square_bad_assertion_usage.py

def square(x):
    assert x >= 0, "only positive numbers are allowed"
    return x ** 2

try:
    print(square(-2))
except AssertionError as error:
    print(error)
