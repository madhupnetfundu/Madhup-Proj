## Command to add two numbers ##
# def myfunc(a,b):
#     ## Returns 5% of the sum of a and b
#     return sum((a,b)) * 0.05

# When we execute
# myfunc(40,60)

# we get :
# 5.0

# Now, consider, we have to pass multiple params :
# def myfunc(*args):
#     return sum(args) * 0.05

# When we execute 
# myfunc(40,60,100)

# we get :
# 10

# args in action:
def myfunc(*args):
    # return sum(args) * 0.05
    total = sum(args)
    print (total)
myfunc(25,25,25,25)