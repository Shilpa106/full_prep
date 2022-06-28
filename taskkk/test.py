

# You are given a string s and an array of string words of the same length. Return all starting indices of		 substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.


# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively. The output order does not matter, returning [9,0] is fine too.


# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []


# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]


# Constraints:

# 1 <= s.length <= 104

# s consists of lower-case English letters.

# 1 <= words.length <= 5000

# 1 <= words[i].length <= 30

# words[i] consists of lower-case English letters.

 

# s = "barfoothefoobarman"
# words = ["foo","bar"] 
# substr=''


#    string:str, substr:s
 
def printIndex(str,s):
    flag=False
    op=[]

    for i in range(len(str)):
        for j in s:
            # print('i',i)
            # print('j',j)
            # print('len',len(j))
            
            if(str[i:i+len(j)]==j):
                op.append(i)
            # print(op)
                # print(i,end='')
                flag=True
            # print(op)
        if (flag==False):
            print('None')
    return op


# s = "barfoothefoobarman"
# words = ["foo","bar"] 

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"] 

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"] 
from itertools import permutations  
words = permutations(words)  
substr3=[]
st=''
for p in list(words):  
    # print(p)
    d=''
    for i in p: 
        # print(i)
        d+=i
    # print(d)
    substr3.append(d)
# print("sbstr",substr3)

print(printIndex(s,substr3))
