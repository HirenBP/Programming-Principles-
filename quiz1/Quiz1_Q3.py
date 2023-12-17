# Ask the user to enter three integers a, b, and c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calculate the absolute differences between the pairs of integers
diff_ab = abs(a - b)
diff_ac = abs(a - c)
diff_bc = abs(b - c)

# Check if the condition is satisfied
condition = (diff_ab >= 10 or diff_ac >= 10 or diff_bc >= 10) and (a < 10 or b < 10 or c < 10)

# Print the result
print(condition)