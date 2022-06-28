Encrypt given Array in single digit using inverted Pascal Triangle

Last Updated : 04 May, 2022
Given an array arr[] of length N (N > 1)containing positive integers, the task is to encrypt the numbers of the array into a single digit using the inverted Pascal triangle as follows.

From the starting of the array find the sum of two adjacent elements.
Replace the sum with only the digit at the unit position of the sum.
Replace all the array elements with the values formed in this way and continue until there are only two elements left.
The last two elements are concatenated together.
Examples:

Input: arr[] = {4, 5, 6, 7}
Output: 04
Explanation:


Pascal’s encryption of [4, 5, 6, 7]

Input: arr[] = {1, 2, 3}
Output: 35
Explanation:


Pascal’s encryption of [1, 2, 3]

Input: arr[] = {14, 5}
Output: 145
Explanation: As there were two elements they are appended together