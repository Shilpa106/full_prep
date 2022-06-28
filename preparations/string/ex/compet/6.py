# Insert character in each duplicate string after every K elements

# Given a string and a character, insert character after every K occurrences.

# Input : test_str = ‘GeeksforGeeks’, K = 2, add_chr = “;” 
# Output : [‘;GeeksforGeeks’, ‘Ge;eksforGeeks’, ‘Geek;sforGeeks’, ‘Geeksf;orGeeks’, ‘Geeksfor;Geeks’, ‘GeeksforGe;eks’, ‘GeeksforGeek;s’] 
# Explanation : All combinations after adding ; after every K elements.

# Input : test_str = ‘GeeksforGeeks’, K = 2, add_chr = “*” 
# Output : [‘*GeeksforGeeks’, ‘Ge*eksforGeeks’, ‘Geek*sforGeeks’, ‘Geeksf*orGeeks’, ‘Geeksfor*Geeks’, ‘GeeksforGe*eks’, ‘GeeksforGeek*s’] 
# Explanation : All combinations after adding * after every K elements. 