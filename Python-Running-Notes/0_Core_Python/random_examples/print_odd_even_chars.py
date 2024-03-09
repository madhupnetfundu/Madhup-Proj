my_string = input('Enter a string ')
my_list1 = list(my_string)
my_list_odd = []
my_list_even = []
for i in range(0, len(my_list1), 2):
    print(my_list1[i], end=' ')
    # my_list_odd=my_list1.append(i)
print("\n", end='')
for i in range(1, len(my_list1), 2):
    print(my_list1[i], end=' ')
