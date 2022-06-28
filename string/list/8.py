# Custom Split Comma Separated Words

# While working with Python, we can have problem in which we need to perform the task of splitting the words of string on spaces.
# But sometimes, we can have comma separated words, which have comma’s joined to words and require to split them separately. 
# Lets discuss certain ways in which this task can be performed.
# Method #1 : Using replace() 
# Using replace() is one way to solve this problem. In this, we just separate the joined comma from string to spaced so that they can be splitted along
#  with other words correctly.
 

# Output : 
# The original string is : geeksforgeeks, is, best, for, geeks 
# The strings after performing splits : [‘geeksforgeeks’, ‘, ‘, ‘is’, ‘, ‘, ‘best’, ‘, ‘, ‘for’, ‘, ‘, ‘geeks’] 

tests='geeksforgeeks, is, best, for, geeks' 
m=tests.split(',')
print(m)
