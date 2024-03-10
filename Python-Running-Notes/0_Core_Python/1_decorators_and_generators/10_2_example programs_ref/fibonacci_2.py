# The cache decorator is used to store the results of the function in a cache.
# Next up, we'll see how to use the lru_cache decorator to store the results of the function in a cache. See fibonacci_3.py

from my_decorator_dnf import timer
from functools import cache

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

@timer
def main():
    for i in range(500):
        print(i, fib(i))
    print("Done")

if __name__ == "__main__":
    main()