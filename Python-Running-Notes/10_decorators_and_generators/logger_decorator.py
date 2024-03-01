def logger(func):
    def wrapper(*args, **kwargs):
        # Log the arguments before calling the function
        print(f"Calling function {func.__name__} with arguments: {args} {kwargs}")
        print(f"Calling function {func.__name__} with arguments: {args} ")        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value after function execution
        print(f"Function {func.__name__} returned: {result}")
        
        return result
    return wrapper

# Example usage
@logger
def add(a, b):
    return a + b

print(add(3, 5))