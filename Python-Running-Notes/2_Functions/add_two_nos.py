from unittest import result


def add_function(num1, num2):
    return num1+num2 
    ## return allows to save the result to a variable.
    ## most functions will use return. Rarely will a function only print().
result = add_function(10, 20)
print (result)