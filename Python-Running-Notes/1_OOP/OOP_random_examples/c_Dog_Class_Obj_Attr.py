class Dog():

    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots=False):
        self.breed = breed
        self.name = name
        # Expect boolean i.e True/False
        if spots not in (True, False):
            raise ValueError("spots must be either True or False")
        self.spots = spots


my_dog = Dog(breed='lab', name='Sammy', spots=True)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.spots)
