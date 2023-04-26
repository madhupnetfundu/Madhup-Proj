class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):

    def speak(self):
        return self.name+' says Woof!'


class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'


fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


# Real life examples of polymorphism include:

# opening different file types - different tools are needed to display Word, pdf and Excel files
# adding different objects - the + operator performs arithmetic and concatenation
