## Look up the section 'Classes as Decorators' on this article https://betterprogramming.pub/decorators-in-python-72a1d578eac4
# from functools import update_wrapper
import functools
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func) # This is to update the wrapper of the class to the function
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say():
    print("Hello!")

say()
say()
say()
say()
print(say.num_calls)