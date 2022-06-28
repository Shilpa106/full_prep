# String slicing in python to check if a string can become empty by recursive deletion.

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.


# Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
# Output : No
# Explanation : In the string it is not possible to make the
#               string empty in any possible manner.

def checkEmpty(input, pattern):
    # if both are empty
    if len(input) == 0 and len(pattern) == 0:
        return 'true'

    # if only pattern is empty
    if len(pattern)==0:
        return 'true'

    while(len(input)!=0):
        # find substring in main string
        index=input.find(pattern)
        print(index)
        
        # check if substring founded or Not
        if (index==(-1)):
            return 'false'

        # slice input string in two parts and concatenate
        input=input[0:index]+input[index + len(pattern):]

    return 'true'

# Driver Program
if __name__ == '__main__':
    input='GEEGEEKSKS'
    pattern='GEEKS'
    print(checkEmpty(input, pattern))


