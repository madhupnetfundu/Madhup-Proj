## Polymorphism Example ##
# Polymorphism is a fundamental concept in object-oriented programming that allows objects to take on many forms. In Python, polymorphism is often achieved through the use of inheritance and method overriding.

# Here's an example of polymorphism in Python using inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def animal_speak(animal):
    print(animal.speak())


dog = Dog("Rufus")
cat = Cat("Whiskers")

animal_speak(dog)  # Output: "Woof!"
animal_speak(cat)  # Output: "Meow!"


# In this example, we have a base Animal class with an empty speak method. The Dog and Cat classes inherit from Animal and override the speak method with their own implementation.

# The animal_speak function takes an Animal object as a parameter and calls its speak method, which will be dynamically bound to the correct implementation based on the type of the object. This is an example of runtime polymorphism, where the behavior of the program is determined at runtime based on the actual type of the object.
