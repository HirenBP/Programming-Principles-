"""Write a program that reads strings typed by the user until a string ending with
    a ‘.’ is entered, then prints the total number of strings that were entered.
"""
string1 =input("Enter a string: ")
if string1.endswith('.'):
    print('1 string was entered')
else:
    count = 1
    while string1.endswith('.') == False:
        string1 = input("Enter a string: ")
        count = count + 1
    print(f'{count} strings were entered')

