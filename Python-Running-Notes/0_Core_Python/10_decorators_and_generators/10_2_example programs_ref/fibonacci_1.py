### Do not run this code, it will take a long time to execute
### This is a simple recursive implementation of the Fibonacci sequence
### It is very slow and inefficient, take a look at the next demo for a better implementation (program name is fibonacci_2.py)

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(500):
        print(i, fib(i))
    print("Done")

if __name__ == "__main__":
    main()