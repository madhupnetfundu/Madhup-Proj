class Dog():

    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    
    ## METHODS ##
    # Methods are essentially functions defined inside the body of the class and they're used to perform
    # operations that sometimes utilize the actual attributes of the object we created.
    # So you can basically think of methods as functions acting on an object that take the object itself
    # into account through the use of the self argument or self keyword.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
    ## Operations/Actions ---> Methods
    def bark (self):
        print ("WOOF")

my_dog = Dog('Lab','Frankie')

# One of the key differences between attributes and methods is in the way we call them.
# Notice that attributes, for ex. my_dog.species, never had open and close parentheses and that's bcoz
# attributes aren't really somehting that you execute. Instead it's just something that's a 
# characteristic of the object that you call back. Its just information there about the actual dog.
#
# Methods on the other hand need to be executed. So that means we need to have the open and close
# parentheses when we do a method call. See below :

my_dog.bark()

# bottom line method ko call karne k liye hamesha method name k baad open and close parentheses lagega.