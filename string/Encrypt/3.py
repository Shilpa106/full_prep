Encrypt the given string with the following operations

Difficulty Level : Medium
Last Updated : 10 Jun, 2021
Given a string s, the task is to encrypt the string in the following way: 

If the frequency of current character is even, then increment current character by x.
If the frequency of current character is odd, then decrement current character by x.
Note: All the operations are circular that is adding 1 to ‘z’ will give ‘a’ and subtracting 1 from ‘a’ will give ‘z’

Examples:

Input :s=”abcda”, x=3 
Output :dyzad 
‘a’ appear 2 times in the string, hence incrementing ‘a’ by 3 becomes ‘d’ 
‘b’ appear 1 times in the string, hence decrementing ‘b’ by 3 becomes ‘y’ 
‘c’ appear 1 times in the string, hence decrementing ‘c’ by 3 becomes ‘z’ 
‘d’ appear 1 times in the string, hence decrementing ‘d’ by 3 becomes ‘a’ 
‘a’ appear 2 times in the string, hence incrementing ‘a’ by 3 becomes ‘d’ 
Hence the string becomes “dyzad”

Input :s=”aabbc”, x=5 
Output :ffggx 
 