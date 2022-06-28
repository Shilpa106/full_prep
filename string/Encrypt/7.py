Count characters of a string which when removed individually makes the string equal to another string

Difficulty Level : Hard
Last Updated : 23 Aug, 2021
Given two strings A and B of size N and M respectively, the task is to count characters of the string A, which when removed individually makes both the strings equal. If there exists several such characters, then print their respective positions. Otherwise, print “-1”.

Examples:

Input: A = “abaac”, B = “abac”
Output: 2
             3 4
Explanation: 
Following removals are possible that can make the strings equal:

Removing A[2] modifies A to “abac”, which becomes equal to B.
Removing A[3] modifies A to “abac”, which becomes equal to B.
Therefore, two possible removals satisfy the conditions.

Input: A = “abs”, B = “bkk”
Output: -1