# Define function to calculate area

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
print(f"Difference between their areas: {difference}.")