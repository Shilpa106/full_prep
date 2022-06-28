Encrypt the string – 2

Last Updated : 28 Jul, 2021
Given a string S consisting of N, lower case English alphabet, it is also given that a string is encrypted by first replacing every substring of the string consisting of the same character with the concatenation of that character and the hexadecimal representation of the size of the substring and then revering the whole string, the task is to find the encrypted string. 

Note: All Hexadecimal letters should be converted to Lowercase letters.

Examples:

Input: S = “aaaaaaaaaaa”
Output: ba  
Explanation:

First convert the given string to “a11” i.e. write, character along with its frequency.
Then, change “a11” to “ab” because 11 is b in hexadecimal.
Then, finally reverse the string i.e “ba”.
Input: S = “abc”
Output: 1c1b1a

