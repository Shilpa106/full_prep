# Convert list of strings and characters to list of characters

# Sometimes we come forward to the problem in which we receive a list that consists of strings and characters mixed and the task we need to perform is converting that mixed list to a list consisting entirely of characters. Let’s discuss certain ways in which this is achieved.

# Method #1 : Using List comprehension
# In this method, we just consider each list element as string and iterate their each character and append each character to the newly created target list.


# Output:
# The original list is : ['gfg', 'i', 's', 'be', 's', 't']
# The list after conversion is : ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

test= ['gfg', 'i', 's', 'be', 's', 't']
a=[]
for i in test:
    # print(i)
    
    for j in i:
        # print(j)
        a.append(j)
print(a)