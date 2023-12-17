# Problem: Write a program that reads whole numbers typed by the user until a zero is entered, then prints the
# number of positive numbers that were entered. Sample run:

# Ask for input number
number = int(input('Enter a number : '))
# Initialize the positive number counter.
pos_num = 0
# Run the loop until condition is met
while number != 0:
    # if number is greater than 0 increment number counter
    if number > 0:
        pos_num += 1
    # Ask for input inside the loop.
    number = int(input('Enter a number : '))
# Print counter
print(f'{pos_num} positive numbers were entered.')