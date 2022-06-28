# Convert List of lists to list of Strings

# Interconversion of data is very popular nowdays and has many applications. In this scenario, we can have a problem in which we need to convert a list of lists, i.e matrix into list of strings. Let’s discuss certain ways in which this task can be performed.

# Method #1 : Using list comprehension + join()
# The combination of above functionalities can be used to perform this task. In this, we perform the task of iteration using list comprehension and join() is used to perform task of joining string to list of strings.


# op:
# The original list : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# The String of list is : ['gfg', 'is', 'best']


test_str=[['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
print(test_str)
t=[]
for i in test_str:
    # print(i)
    s=''
    for j in i:
        print(j)
        s+=j
    print(s)
    t.append(s)
print(t)
