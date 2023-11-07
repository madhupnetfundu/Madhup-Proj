class Sample():
    pass

my_Sample = Sample()

print (type(my_Sample))

"""
what this code does:

It defines a class named Sample but doesn't specify any attributes or methods, so the class is empty.
It creates an instance of the Sample class and assigns it to the variable my_Sample. This means you now have an object of the Sample class.
It prints the type of the my_Sample object, which will be the class type that the object belongs to, in this case, Sample.
When you run this code, it will print something like:
<class '__main__.Sample'>
Here, __main__ is the name of the current module (the script itself), and Sample is the class name. This output shows that the my_Sample object is of class type Sample in the __main__ module.
"""