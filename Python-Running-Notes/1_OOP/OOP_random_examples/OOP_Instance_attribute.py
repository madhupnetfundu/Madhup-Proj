# 🤩
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
print(miles)    

## The advantage of using the __str__() method in the program you provided is that it allows you to customize the string representation of the Dog object. The __str__() method is a special method that is called when you try to convert an object to a string. In this case, when you print the miles object, the __str__() method is called and the string "Miles is 4 years old" is returned.
## If you do not define a __str__() method, the default string representation of the object will be used. The default string representation is not very user-friendly and it does not provide any information about the object.
