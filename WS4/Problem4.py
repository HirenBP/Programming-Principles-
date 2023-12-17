# Ask for input from user and leave it as string to compare reverse.
number = input('Enter a positive number : ')

# Print Palindrome if reverse is equal to original
print('Number is Palindrome ' if number == number[::-1] else 'Number is not palindrome')
