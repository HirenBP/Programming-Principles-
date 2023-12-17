# A program to output the first n Fibonacci numbers
# Input: n, a positive integer
# Output: a S_list of n Fibonacci numbers, formatted with at most four numbers per row

# Get the input from the user
n = int(input("Enter a positive integer: "))
# Initialize the S_list of Fibonacci numbers
fib_list = [0, 1]
# Calculate the Fibonacci numbers using a loop
for i in range(2, n):
    # The next Fibonacci number is the sum of the previous two
    next_fib = fib_list[i-1] + fib_list[i-2]
    # Append the next Fibonacci number to the S_list
    fib_list.append(next_fib)
counter = 0
for num in fib_list:
    # Print the number with a space after it
    print(num, end=" ")
    # Increment the counter
    counter += 1
    # If the counter reaches four, print a new line and reset the counter
    if counter == 4:
        print()
        counter = 0
