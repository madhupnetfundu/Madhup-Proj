class Cars:
    motor_type = "somecar"

    def __init__(self, color, model):
        self.color = color
        self.model = model

car1=Cars("red", 1)
car2=Cars("white", 2)

print ("car1 is {} in color , model is {} and car2 is {} in color, model is {}".format(car1.color, car1.model, car2.color, car2.model))

# class Dog:
#     species="mammal"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# dog1=Dog("doggie1",4)
# dog2=Dog("doggie2",5)

# print (dog1.age)
# print (dog2.name)
# print("{} is {} years old and {} is {} years old".format(dog1.name, dog1.age, dog2.name, dog2.age))