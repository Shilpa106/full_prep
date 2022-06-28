
# Find all duplicate characters in string

# Input : hello
# Output : l

# Input : geeksforgeeeks
# Output : e g k s

t='hello'
# # print(t)
# for i in t:
#     # print(t.count(i))
#     if t.count(i)>1:
#         print(i)


# # EX2
# from collections import Counter

# def find_dup_char(input):
#     # now create dictionary using counter method which will have Strings
#     # as key and their frequencies as values
#     WC=Counter(input)

#     # finding no. of occurrences of a character and get the index of it.
#     for letter ,count in WC.items():
#         if(count>1):
#             print(letter)

# # 
# if __name__ == '__main__':
#     input='geeksforgeeks'
#     find_dup_char(input)

# M1: Using hashing
# algo: let input geeksforgeeks
# 1.construct character count array from the input string
# count['e']=4
# count['g']=2
# count['k']=2

# 2.Print all the indexes from the constructed array which have value greater than 1.

# count all duplicates using hashing
NO_OF_CHARS=256

# Fills count array with frequency of characters
def fillCharCounts(string, count):
    for i in string:
        count[ord(i)]+=1
    return count 

# Print duplicates present in the passed string
def printDups(string):
    # create an array of size 256 and fill count of every character in it.
    count=[0]*NO_OF_CHARS
    count=fillCharCounts(string, count)

    # Utility variable
    k=0

    # print characters having count more than 0
    for i in count:
        if int(i)>1:
            print( chr(k) + ", count=" +str(i))
        k+=1
string="test string"
print(printDups(string))
