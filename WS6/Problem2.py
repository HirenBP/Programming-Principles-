"""
Problem: Write a program that allows the user to enter two lists of integers, calculate the sum of the first
and the last integers in each list, and print the larger sum. In the event of a tie, print Same. When there is
only one integer in the list, the sum is the integer itself.
"""
# Ask for inputs
s1 = input('List 1: ')
s2 = input('List 2: ')
# Convert string into int and store in a list
l1 = [int(i) for i in s1.split()]
l2 = [int(i) for i in s2.split()]

# Calculate both sums if length of list is 1 first int in list is the sum
sum1 = l1[0] + l1[-1] if len(l1) > 1 else l1[0]
sum2 = l2[0] + l2[-1] if len(l2) > 1 else l2[0]
# Print larger sum or same in case of tie
print('Output:', max(sum1, sum2) if sum1 != sum2 else 'Same')
