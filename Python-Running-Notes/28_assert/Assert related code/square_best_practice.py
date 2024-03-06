# square_best_practice.py

def square(x):
    if x < 0:
        raise ValueError("only positive numbers are allowed")
    return x ** 2

try:
    print(square(-2))
except ValueError as error:
    print(error)
