# creating a string with single quotes

# string1='wlerjlkdjf'
# print(string1)

# creating a string with double quotes

# string2="fjdkljf"
# print(string2)

# creating a string with triple quotes

# string3="""hey how are you???"""
# print(string3)

# creating a string with triple quotes allows multiple lines

# string4='''Geeks
#           For
#           Life '''

# print('creating  a multiline string with triple quotes',string4)

# Accessing character in python

# string='geeksforgeeks'
# # print(string[0])
# print(string[-1])


# updating or deleting a string 
# updation or deletion of character from a string is not allowed.This will cause an error because item assignment or item deletion from a string is not supported.
# although deletion of the entire string is possible with the use of a builtin del keyword.this is  because strings are immutable.hence element of a string can
#  not be changed once it has been assigned.only new strings can be reassigned to the same name.
# string1="hello ,shilpi here"

# string[1]='l'
# print(string)

# del string1[2]
# print(string1)

#del

# update entire string 
# string='geeksforgeeks'
# string='fdfdf'
# print(string)

# delete entire string
# del string
# print(string)



# Escape Sequencing in python
# string1='''I'm a "geeks"'''
# print(string1)

# Escaping Single quote
# string1='I\'m a "geeks"'
# print(string1)

# Escaping Double quotes
# string1="I\'m a \"geeks\""
# print(string1)

# printing paths with the use of escape sequences
# string1="C:\\Python\\Geeks\\"
# print(string1)

# string="This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print(string)

# # using raw string to ignore escape sequences
# string=r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print(string)

# Formatting of string
# Default Order
# string="{}{}{}".format('geeks','for','life')
# print(string)

# Positional Formatting
# string="{1}{0}{2}".format('geeks','for','life')
# print(string)

# # keyword formatting
# string="{l}{f}{g}".format(g='geeks',l='life',f='for')
# print(string)

# Formatting of integers
# string="{0:b}".format(16)
# print(string)

# Formatting of floats
# string="{0:e}".format(165.6458)
# print(string)

# Rounding off integers
# string="{0:.2f}".format(1/6)
# print(string)


# # string alignment
# string="|{:<10}|{:^10}|{:>10}|".format('geeks','for','geeks')
# print(string)

# # Aligning of spaces
# string="\n{0:^16} was founded in {1:<4}!".format("geeksforgeeks",2009)
# print(string)


# String formatting in python using %

# Integer1=12.3456789
# # print(Integer1)
# print('The value of Integer1 is %3.2f' % Integer1)
# print('The value of Integer1 is %3.4f' % Integer1)s


# Logical operators on string in python
# str1=''
# str2='geeks'

# repr is used to print the string along with quotes

# Returns str1
# print(repr(str1 and str2))
# print(repr(str2 and str1))

# print(repr(str1 or str2))
# print(repr(str2 or str1))


# str1='for'
# print(repr(str1 and str2))
# print(repr(str2 and str1))


# print(repr(str1 or str2))
# print(repr(str2 or str1))


# str1='geeks'
# print(repr(not str1))


