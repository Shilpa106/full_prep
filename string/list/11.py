# Convert list of string to list of list

# Many times, we come over the dumped data that is found in the string format and we require it to be represented into the actual list format
# in which it was actually found. This kind of problem of converting a list represented in string format back to list to perform tasks is quite common
#  in web development. Let’s discuss certain ways in which this can be performed.

# Method #1 : Using strip() + split()
# A combination of strip and split function can perform a particular task. The strip function can be used to get rid of the brackets and split function can make the data list comma-separated.


# The original list is : ['[1, 4, 5]', '[4, 6, 8]']
# The list after conversion is : [['1', ' 4', ' 5'], ['4', ' 6', ' 8']]

import ast
m=[]
tests= ['[1, 4, 5]', '[4, 6, 8]']
print(tests)
for i in tests:
    # print(i.split())
    p=ast.literal_eval(i)
    # p.split()
    print("ppppppppppppppp",p)
    # for l in p:
    #     l.split("")
    #     print(l)
    m.append(p)
print(m)
for k in m:
    for s in k:
        ss=str(s)
        print(ss)
    print(k)
    # print(p)
    # print(type(p))

