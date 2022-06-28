# Convert key-value pair comma separated string into dictionary

# Given a string, with different key-value pairs separated with commas, the task is to convert that string into the dictionary.
# These types of problems are common in web development where we fetch arguments from queries or get a response in the form of strings.
#  Given below are a few methods to solve the task.

# Method #1: Using dictionary comprehension


# # Python3 code to demonstrate 
# # converting comma separated string
# # into dictionary
  
# # Initialising string
string = 'name = akshat, course = btech, branch = computer'
res= dict(item.split("=")for item in string.split(","))
print(res)
print(type(res))
  