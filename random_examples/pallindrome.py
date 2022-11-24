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
