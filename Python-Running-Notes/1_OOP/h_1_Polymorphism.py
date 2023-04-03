## Polymorphism
# We've learned that while functions can take in different arguments, methods belong to the objects they act on. In Python, *polymorphism* refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in. The best way to explain this is by example:

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# Here we have a Dog class and a Cat class , and each has a .speak() method. When called, each object's .speak() method returns a result unique to the object.

# There a few different ways to demonstrate polymorphism. First, with a for loop:

for pet in [niko, felix]:
    print(pet.speak())


# Another is with functions:
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

# In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.

# A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals. See Polymorphism_2.py
#