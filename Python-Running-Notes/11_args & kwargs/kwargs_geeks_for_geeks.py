#Here **kwargs accept keyworded variable-length argument passed by the function call. for first=’Geeks’ first is key and ‘Geeks’ is a value. in simple words, what we assign is value, and to whom we assign is key
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
