# String constants 

# string.ascii_letters  : Concatenation of the ascii_lowercase and ascii_uppercase constants.

import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits) #0123456789abcdefABCDEF
# string.letters,string.lowercase
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable) # string of characters which are printable

# string endswith() method
# str.endswith(suffix,start,end)
# suffix:string that need to be checked 
# start: from where suffix to be checked in string
# end: end pos+1 from which suffix is to be checked
#  if starting and end pos is not provided by default then it takes 0 and len-1 where ending index is not included in search string.

# # ex1
# text='geeks for geeks.'
# # result=text.endswith('for geeks') #false
# # result=text.endswith('geeks.') #true
# # result=text.endswith('for geeks.') #true
# result=text.endswith('geeks for geeks.')
# print(result)


# # ex2
# # working of endswith() method with start and end parameters
# text="geeks for geeks."
# # result=text.endswith('geeks.',10) # start parameters is provided

# # both start and end is provided start =10 end =16-1 
# # result=text.endswith('geeks',10,16) #false
# result=text.endswith('geeks',10,15) #true
# print(result)

# # real world ex
# print("***Valid Geeksforgeeks Email Checker***\n")
# user_email=input("Enter your GFG Official Mail:").lower()
# if user_email.endswith("@geeksforgeeks.org"):
#     print('hello geeks')
# else:
#     print('Invalid, A Stranger detected')


# string startswith()
# str.startswith(prefix,start,end)
# text='geeks for geeks.'
# # result=text.startswith('for geeks')
# # result=text.startswith('geeks')
# # result=text.startswith('for geeks.')
# result=text.startswith('geeks for geeks.')
# print(result)

# string='15460'
# string='154ayush60'
# print(string.isdigit())


# # txt="CompanyX"
# txt="Company34"
# x=txt.isalpha()
# print(x)

# s="12345"
# print(s)
# print(s.isdecimal())

# s="12geeks34"
# print(s.isdecimal())

# s="12 34"
# print(s.isdecimal())

# ex1
# import string

# # Storing the value in variable result
# result=string.ascii_letters
# print(result)

# ex2.
# # check if the string input has only ASCII characters or not.
# import string
# def check(value):
#     for letter in value:
#         if letter not in string.ascii_letters:
#             return False
#     return True

# input1='GeeksForGeeks'
# print(input1,'-->', check(input1))

# input2='Geeks for Geeks'
# print(input2,'-->', check(input2))

# input3="Geeks_for_geeks"
# print(input3,'-->', check(input3))


# # ex
# import random
# a='shilp1234'
# for n in range(4):
#     # b=''.join(random.choice(a))
#     # b=random.choice(a)
#     print(b)

# a=''.join(['hey' for n in range(4)])
# print(a)



#  use ascii_letters to generate strong random passwords of given size
# ex1
# import random
# import string
# def rand_pass(size):
#     # Takes random choices from ascii_letters and digits to generate
#     # print(string.ascii_letters)
#     # print(string.digits)
#     # print(string.ascii_letters+string.digits)
#     print(random.choice(string.ascii_letters+string.digits))
#     generate_pass=''.join([random.choice(string.ascii_letters+string.digits) for n in range(size)])
#     return generate_pass

# password=rand_pass(10)
# print(password)

# ex2
# generate random password , but from the set of given string.
# import random
# import string

# def rand_pass(size, scope=string.ascii_letters+string.digits):
#     # Takes random choices from ascii_letters and digits 
#     generate_pass=''.join([random.choice(scope) for n in range(size)])
#     return generate_pass

# passwords=rand_pass(10,'shilpayadav1033984384')
# print(passwords)


# # string formatting
# print("{}, A computer science portal for geeks.".format("GeeksforGeeks"))

# # using format option for a value stored in a variable 
# str="This article is written in {}"
# print(str.format("Python"))

# # formatting a string using a numeric constants
# print("Hello, I am {} years old !".format(18))


# ex2  Python string format() method indexerror
# my_string="{}, is a {} {}  science portal for {}"
# print(my_string.format("GeeksforGeeks","computer","geeks"))


