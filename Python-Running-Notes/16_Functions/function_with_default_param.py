# def say_hello(name):
#     print(f'Hello {name}')
# say_hello("Madhup")

# If we execute the above program without providing the name then it will throw an error saying that :
# say_hello() is missing one required positional argument : 'name'

# So, we can provide a default value so that if the name is not provided whatever default string we have mentioned in the code will be used.
# Consider this :
def say_hello(name="Default"):
    print(f'Hello {name}')
say_hello()
say_hello("Madhup")


