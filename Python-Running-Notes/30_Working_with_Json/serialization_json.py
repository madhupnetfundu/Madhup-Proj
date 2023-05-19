# 💡 Serializing json
# What happens after a computer processes lots of information? 
# It needs to take a data dump. Accordingly, the json library exposes the dump() method for writing data to files. 
# There is also a dumps() method(pronounced as “dump-s”) for writing to a Python string.

# Simple Python objects are translated to JSON according to a fairly intuitive conversion :
# Python 	                    JSON
# dict 	                        object
# list, tuple 	                array
# str 	                        string
# int, long, float 	            number
# True 	                        true
# False 	                    false
# None 	                        null


import json
# Imagine you’re working with a Python object in memory that looks a little something like this:
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# It is critical that you save this information to disk, so your mission is to write it to a file.
# Using Python’s context manager, you can create a file called data_file.json and open it in write mode. (JSON files conveniently end in a .json extension.)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# 👉 Note that dump() takes two positional arguments: 
# (1) the data object to be serialized, and 
# (2) the file-like object to which the bytes will be written.

# Or, if you were so inclined as to continue using this serialized JSON data in your program, 
# you could write it to a native Python str object :
json_string = json.dumps(data)

# 👉Notice that the file-like object is absent since you aren’t actually writing to disk. Other than that, dumps() is just like dump().

# 👉 Both the dump() and dumps() methods use the same keyword arguments. 

# Primer on keyword arguments_good one: 
# https://www.educative.io/answers/what-are-keyword-arguments-in-python

# The first option most people want to change is whitespace. You can use the indent keyword argument to specify the indentation size 
# for nested structures. Check out the difference for yourself by using data, which we defined above, and running the following 
# commands in a console:
#>>> json.dumps(data)
#>>> json.dumps(data, indent=4)

# Another formatting option is the separators keyword argument. By default, this is a 2-tuple of the separator strings (", ", ": "), 
# but a common alternative for compact JSON is (",", ":"). Take a look at the sample JSON again to see where these separators come into play.

# Printing the below just out of curiosity
print (json_string)

