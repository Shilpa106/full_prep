# Remove all duplicates from a given string in Python


# We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters?

# Examples:

# Input : geeksforgeeks
# Output : efgkors

s='geeksforgeeks'
li=list(s)
p=[]
for i in li:
    if i not in p:
        p.append(i)

print(p)