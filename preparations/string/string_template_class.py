

# String Template Class in Python
from string import Template


# # create a template that has placeholder for value of x
# t=Template('x is $x')

# # substitute value of x in above template
# print(t.substitute({'x':1}))


# # EX2
# Student=[('Ram',90),('Ankit',78),('Bob',92)]
# t=Template('HI $name, you have got $marks marks')
# for i in Student:
#     print(t.substitute(name=i[0],marks=i[1]))


# safe_substitute method
# Example 3:

# template=Template('$name is the $job of $company')
# string=template.safe_substitute(name='shilpa y',job='it')
# print(string)


# # EX4
# t=Template('I am $name from $city')
# print('Template String: ',t.template)

# Escaping $ sign
# The $$ can be used to escape $ and treat as part of the string
# ex

# $$ is used to escape $ and print $ as a string

# template=Template('$$ is the symbol for $name')
# string=template.substitute(name='Dollar')
# print(string)

# The ${Identifier}
template=Template('That $noun looks ${noun}y')
string=template.substitute(noun='Fish')
print(string)