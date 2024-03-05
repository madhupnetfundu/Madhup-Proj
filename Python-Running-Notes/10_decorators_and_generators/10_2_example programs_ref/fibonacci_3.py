from functools import lru_cache
from my_decorator_dnf import timer

#@lru_cache # This is the same as @cache, but it has a maximum size of 128. If the cache is full, it will discard the least recently used item.
@lru_cache(maxsize=5) # This is how you can set the maximum size of the cache. If the cache is full, it will discard the least recently used item.
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

# The lru_cache decorator is used to store the results of the function in a cache. 