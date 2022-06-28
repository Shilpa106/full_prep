x=10
y=x
if id(x)==id(y):
    print("x and y refer to the same object")

x+=1
if id(x)!=id(y):
    print("x and y refer to different objects")


# Memory Allocation in Python
# These are 2 parts of memory
# stack memory
# heap memory

# The methods/method calls and the references are stored in stack memory and all the values objects 
# are stored in private heap

