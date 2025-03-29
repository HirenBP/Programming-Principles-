
"""
Write a program that takes as input the lengths and the widths of two rectangles.
Calculate the difference between the areas of two rectangles. Print the result as shown
in the example below.
Example:

Length of the first rectangle: 10

Width of the first rectangle: 8

Length of the second rectangle: 7

Width of the second rectangle: 5

Difference between their areas: 45
"""

def area(length, width):
    return length * width

# Ask the user to enter the lengths and widths of two rectangles
length1 = int(input("Length of the first rectangle: "))
width1 = int(input("Width of the first rectangle: "))
length2 = int(input("Length of the second rectangle: "))
width2 = int(input("Width of the second rectangle: "))

# Calculate the areas of the two rectangles
area1 = area(length1, width1)
area2 = area(length2, width2)

# Calculate the difference between the areas
difference = abs(area1 - area2)

# Print the result
print(f"Difference between their areas: {difference}")