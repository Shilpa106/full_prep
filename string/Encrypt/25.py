Modify the string such that every character gets replaced with the next character in the keyboard

Last Updated : 14 May, 2021
Given a string str consisting of lowercase English alphabets. The task is to change each character of the string with the next letter (in a circular fashion) key in the keyboard. For example, ‘a’ gets replaced with ‘s’, ‘b’ gets replaced with ‘n’, ….., ‘l’ gets replaced with ‘z’, ….., ‘m’ gets replaced with ‘q’.
Examples: 
 

Input: str = “geeks” 
Output: hrrld
Input: str = “plmabc” 
Output: azqsnv 
 

 

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach: For every lowercase character of the English alphabet, insert the character next to it in the keyboard in an unordered_map. Now traverse the given string character by character, and update every character with the map created earlier.