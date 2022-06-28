# Program to check if input is an integer or a string

# Input : 127
# Output : Integer
# Explanation : All digits are in the range '0-9'.

# Input : 199.7
# Output : String
# Explanation : A dot is present. 

# Input : 122B
# Output : String
# Explanation : A alphabet is present.


# def isNumber(s):
#     for i in range(len(s)):
#         if s[i].isdigit()!=True:
#             return False
#     return True

# if __name__ == "__main__":
#     str='4p34'
#     if isNumber(str):
#         print("Integer")
#     else:
#         print("String")


# Quick way to check if all the characters of a string are same
# Input : s = "geeks"
# Output : No

# Input : s = "gggg" 
# Output : Yes

# def allCharactersSame(s):
#     for i in range(1, len(s)):
#         if s[i]!=s[0]:
#             return False
#     return True

# if __name__ =="__main__":
#     s='aaua'
#     if allCharactersSame(s):
#         print("Yes")
#     else:
#         print("No")


# Program to find the initials of a name.
# Input  : prabhat kumar singh
# Output : P K S
# We take the first letter of all
# words and print in capital letter.

# Input  : Shilpa yadav
# Output : S Y

# Input  : abhishek kumar singh
# Output : A K S
# s='Shilpa yadav'
# a=s.split()
# # print(len(a))
# for i in range(len(a)):
#     print(a[i][0].capitalize(), end=' ')








# def copy_str(x,y):
#     if len(y)==0:
#         return x
#     else:
    
#         c=copy_str(x,(y)[1:-1])
#         return c

# x=input()
# y=input()
# print(copy_str(x,y))


# non repeating characters
# Input: "geeksforgeeks"
# s="geeksforgeeks"
# for i in range(len(s)):
#     if s.count(s[i])==1:
#         print(s[i],end=" ")


# Removing punctuations from a given string
# Input : %welcome' to @geeksforgeek<s
# Output : welcome to geeksforgeeks

# Input : Hello!!!, he said ---and went.
# Output : Hello he said and went

# punctuations="!$%&'()*+,-./:;?@<[\]^_`'{|}~"
# s="%welcome' to @geeksforgeek<s"
# for i in s:
#     if i in punctuations:
#         s=s.replace(i,'')
# print(s)

# *******************************
# # Rearrange characters in a string such that no two adjacent are same
# # Input: aaabc 
# # Output: abaca 

# # Input: aaabb
# # Output: ababa 

# # Input: aa 
# # Output: Not Possible

# # Input: aaaabc 
# # Output: Not Possible

# st='aaabc'
# for i in range(len(st)):
#     # print("tttttttttt",st.count(st[i]))
#     j=i-1
#     if st[j]!=st[i]:
        
#         print(st[i],end='')


# ***********************************************


    



