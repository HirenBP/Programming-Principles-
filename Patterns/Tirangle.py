# Steps to Print Pattern in Python
# Use the below steps to print a pattern in Python
#
# Decide the number of rows and columns
# There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops
# to print any pattern, i.e., use nested loops.
#
# The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.
#
# Accept the number of rows from a user using the input() function to decide the size of a pattern.
#
# Iterate rows
# Next, write an outer loop to Iterate the number of rows using a for loop and range() function.
#
# Iterate columns
# Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends
# on the values of the outer loop.
#
# Print star or number
# Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern
# (like a star (asterisk *) or number).
#
# Add a new line after each iteration of the outer loop
# Add a new line using the print() function after each iteration of the outer loop so that the pattern
# display appropriately

# To print triangle pattern
#
##
###
####
#####
rows = int(input('Plese enter number of rows :'))
# Outer loop
for i in range(rows+1):
    #nested loop
    for j in range(i):
        print('x',end='')
    # New line
    print()