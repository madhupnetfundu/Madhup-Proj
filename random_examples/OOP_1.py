class Dog:
    species="mammal"

    def __init__(self,name,age):
        self.name = name
        self.age = age
dog1=Dog("doggie1",4)
dog2=Dog("doggie2",5)

print (dog1.age)
print (dog2.name)
print("{} is {} years old and {} is {} years old".format(dog1.name, dog1.age, dog2.name, dog2.age))