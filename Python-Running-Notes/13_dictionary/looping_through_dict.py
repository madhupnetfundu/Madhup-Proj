# Example on how to iterate through a dict :
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Print all key names in the dictionary, one by one:
print("printing keys ONLY")
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
print()
print("*" * 50)
print()

#  prints values only 
print("printing values ONLY")
for x in thisdict:
  print(thisdict[x])
print()

# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)
