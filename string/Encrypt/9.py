Shortest distance to every other character from given character

Difficulty Level : Medium
Last Updated : 19 Apr, 2022
Given a string S and a character X where X\varepsilon S[i]            , for some 0\leq i \leq S.length()-1            . The task is to return an array of distances representing the shortest distance from the character X to every other character in the string.
Examples: 

Input: S = “geeksforgeeks”, X = ‘e’ 
Output: [1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2] 
for S[0] = ‘g’ nearest ‘e’ is at distance = 1 i.e. S[1] = ‘e’. 
similarly, for S[1] = ‘e’, distance = 0. 
for S[6] = ‘o’, distance = 3 since we have S[9] = ‘e’, and so on.
Input: S = “helloworld”, X = ‘o’ 
Output: [4, 3, 2, 1, 0, 1, 0, 1, 2, 3] 