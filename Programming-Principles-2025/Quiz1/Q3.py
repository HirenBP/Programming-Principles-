"""
Input three integers a, b, and c. Sort them in descending order.
With the sorted integers, print True if the differences between every two neighbouring numbers are the same.
Otherwise, print False. (Python sort(), sorted(), max(), and min() functions are not allowed.)
Example:

a: 10
b: 30
c: 20
Output: True
"""

# Function to sort and check condition
def check_differences(num1, num2, num3):
    # Sorting the integers manually in descending order
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2

    # Checking if the differences between neighboring numbers are equal
    if (num1 - num2) == (num2 - num3):
        return True

    return False

# Ask the user to enter three integers a, b, and c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Print the result
print(f'Output: {check_differences(a,b,c)}')
