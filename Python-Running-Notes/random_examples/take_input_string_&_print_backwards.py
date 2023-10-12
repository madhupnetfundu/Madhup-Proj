my_string = input('pls enter a string ')
my_list = list(my_string)
my_list.reverse()
# print(my_list)
for i in range(len(my_list)):
    print (my_list[i], end='') #use end='' to print horizontally
