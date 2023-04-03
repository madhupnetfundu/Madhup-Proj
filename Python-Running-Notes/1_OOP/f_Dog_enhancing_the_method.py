class Dog():

    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog('Lab', 'Frankie')
my_dog.bark(10)
