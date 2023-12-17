"""
Problem: Write a program that reads strings (without digits or symbols in the string) typed by the user until
an empty string is entered. For each string, convert all words to lowercase, then sort and print the words into
descending order lexicographically.
Hint: use split function to split a string into a S_list, then sort it with a method.
"""
# Ask for input string
s = input('Please enter string : ')
#Loop until input is empty string
while s != "":
    # split and lower the string and store in list
    S_list = s.lower().split(" ")
    # Sort with descending order
    S_list.sort(reverse=True)
    # Print the output
    print('Output: ', *S_list)
    # Ask for input string inside the loop
    s = input('Enter a string : ')