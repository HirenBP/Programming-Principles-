# Problem3
# Write a program that takes as input 3 integers and outputs them in descending order.
a = int(input("Integer 1? "))
b = int(input("Integer 2? "))
c = int(input("Integer 3? "))
print('Sorted', *sorted([a, b, c], reverse=True))