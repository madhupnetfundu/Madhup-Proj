my_msg = "hello world!"
# print (type(my_msg))
# my_msg.split()
# print(my_msg.split())
my_lst = my_msg.split()
# lst =  "Geeks For geeks"
# print( lst.split())
print("original string was " + my_msg)
print(my_lst)


# Some of the examples are :
# 1. Write a command to take name as input and store and prints them in a list.
# 2. enter two nos in a list
# 3. Pallindrome

#### Pallindrome ####
my_string = input('enter a string? ')
my_list1 = list(my_string)
print("turning string into my_list1", str(my_list1))
my_list2 = my_list1.copy()
print("printing my_list2 after copying from my_list1", str(my_list2))
my_list1.reverse()
print("printing my_list1 after reverse", str(my_list1))

print("comparing strings")

if my_list1 == my_list2:
    print('Yes its a palindrome')
else:
    print('Not a palindrome')





# take input as name, put them in a split and print it 