import json
# In the json library, you’ll find load() and loads() for turning JSON encoded data into Python objects.

# Just like serialization, there is a simple conversion table for deserialization, though you can probably guess what it looks like already.
# JSON 	            Python
# object      	    dict
# array 	        list
# string 	        str
# number(int) 	    int
# number(real) 	    float
# true 	            True
# false 	        False
# null 	            None

# Technically, this conversion isn’t a perfect inverse to the serialization table. That basically means that if you encode an object now and 
# then decode it again later, you may not get exactly the same object back. It’s probably more like getting one friend to 
# translate something into Japanese and another friend to translate it back into English. Regardless, the simplest example would be encoding
#  a tuple and getting back a list after decoding, like so:
# >>> blackjack_hand = (8, "Q")
# >>> encoded_hand = json.dumps(blackjack_hand)
# >>> decoded_hand = json.loads(encoded_hand)

# >>> blackjack_hand == decoded_hand
# False
# >>> type(blackjack_hand)
# <class 'tuple' >
# >>> type(decoded_hand)
# <class 'list' >
# >>> blackjack_hand == tuple(decoded_hand)
# True


# Deserialization Example :
# This time, imagine you’ve got some data stored on disk that you’d like to manipulate in memory. You’ll still use the context manager, 
# but this time you’ll open up the existing data_file.json in read mode.
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

# Things are pretty straightforward here, but keep in mind that the result of this method could return any of the allowed data types from 
# the conversion table. This is only important if you’re loading in data you haven’t seen before. In most cases, the root object will be a 
# dict or a list.
# If you’ve pulled JSON data in from another program or have otherwise obtained a string of JSON formatted data in Python, you can easily 
# deserialize that with loads(), which naturally loads from a string:
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
