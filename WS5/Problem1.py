"""
Problem: Write a program that prompts for and reads strings until a string that starts with the letter “A” is entered
(inclusive), then prints the longest string that was entered.  Sample run:

Enter a string: Jaypher said, ’It’s safer
Enter a string: you’ve lemons in your head;
Enter a string: First to eat, a pound of meat,
Enter a string: Find then to go at once to bed.
Enter a string: Eating meat is half the battle,
Enter a string: Will you hear the Lemons rattle!
Enter a string: If you don’t, you’ll always moan,
Enter a string: In a Lemoncolly tone;
Enter a string: For there’s nothing half so dreadful,
Enter a string: As Lemons in your head.
Longest was: 'For there’s nothing half so dreadful,'

"""
# Ask for user input
Strings = input('Enter a string: ')
# Initialize str variable to store longest string
longestString = ""
# Use startswith() function that returns boolean as condition.
while not Strings.startswith('A'):
    # If string is empty ask for another input.
    if not Strings:
        print("String can not be empty")
    # if the length of input is greater than longestString assign value of Strings to longestStrings
    if len(Strings) > len(longestString):
        longestString = Strings
    # Ask for input inside the loop
    Strings = input('Enter a string: ')
print(f"""Longest was: '{longestString}'""" )


