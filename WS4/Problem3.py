# Ask for input and
n = int(input('Enter a positive number : '))
# Outer loop to print number of rows
for i in range(1, 2*n):
    # 1st inner loop to print spaces
    for j in range(abs(n-i)):
        print(" ",end='')
    # 2nd inner loop to print 'x'
    for k in range(2*(n - abs(n-i)) - 1):
        print('x',end='')
    # Add print() to enter new line
    print()
