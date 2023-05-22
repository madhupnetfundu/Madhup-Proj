# 🤩--> nice
# Special Methods
# Finally let's go over special methods. Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print(book)
print(len(book))
del book

# The __init__(), __str__(), __len__() and __del__() methods
# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class .

# The line del book in the program you provided deletes the book object from memory. This is done by using the del keyword, which is used to delete variables and objects in Python. When the book object is deleted, the __del__() method is called. The __del__() method is a special method that is called when an object is deleted. In this case, the __del__() method prints the message "A book is destroyed".

# The del keyword can be used to delete any variable or object in Python. However, it is important to note that deleting an object can have side effects. For example, if the object is being used by another object, deleting the object may cause the other object to fail. Therefore, it is important to be careful when deleting objects in Python.

# Here is a breakdown of what happens when the del book statement is executed:

# The del keyword is used to delete the book variable.
# The __del__() method is called on the book object.
# The book object is removed from memory.
# The __del__() method is a special method that is called when an object is deleted. The __del__() method is not called directly, but it is called by the del keyword. The __del__() method can be used to perform cleanup tasks when an object is deleted. For example, the __del__() method can be used to close files or release resources.

# In the example you provided, the __del__() method prints the message "A book is destroyed". This message is printed to indicate that the book object has been deleted.