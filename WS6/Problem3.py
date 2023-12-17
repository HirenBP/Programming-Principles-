"""
Problem: We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately
 to its left or right.
 Write a function to print True if all the g’s in the given string are happy, otherwise, print False.
"""

# Function to find happy g in given string returns True or False
def findg(a):
    return 'gg' in a
# Ask for user Input
s1 = input('String:')
# Print is happy g is present in given string
print('IsHappy?:', findg(s1))