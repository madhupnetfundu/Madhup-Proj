class Dog():
    
    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # Expect boolean i.e True/False
        self.spots = spots


my_dog = Dog(breed='lab', name='Sammy', spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
