class Dog():

    def __init__(self, breed,name,spots):
        self.breed = breed
        self.name  = name
        # Expect boolean i.e True/False
        self.spots = spots


my_dog = Dog(breed='lab', name='Sammy', spots=False)
print(my_dog.breed)