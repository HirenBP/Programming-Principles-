"""
Problem: Write a program with a function that converts all numerical digits in a string to underline.
Sample run:
Input a string? Australia has 59,736 km coastal line
Output: Australia has __,___ km costal line.
Input a string? 10 X 10 = 20
"""
# Ask user for input
s = input('Input a string? ')
# String is a iterable object. Below loop assigns each character of string s to i
for i in s:
    # Check condition if the given character is numerical by using built in function isdigit()
    if i.isdigit():
        # If the given character is digit we can replace that character with _ by using another
        # built-in function for string replace(oldvalue, newvalue)
        # it is important to assign replaced value to s again in the function
        s = s.replace(i, '_')
print(s)

