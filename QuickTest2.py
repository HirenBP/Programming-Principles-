"""
Prblem : Create a list of numbers from 1 to 15. Using map function store each element of list and it's square in
a tupple in a new list called squrd_list. Hint : Use map function
"""
list1 = list(range(1,16))
squrd_list = list(map(lambda x: (x,x ** 2), list1))
print(squrd_list)

# Filter squred list where the first element of stored touples are odd

fltr_list = list(filter(lambda x: x[0] % 2 == 0, squrd_list))
print(fltr_list)

# Now map and filter both in the same assignemtnt to the list object.

combined_list = list(map(lambda x: (x, x ** 2),
                         filter(lambda x: x % 2 == 0, list1)))

print(combined_list)

# Now perform same operation without using lambda and define your own functions.
def num_squrd(num):
          return num ** 2
def num_even(num):
    if num % 2 == 0: return num

combined_list_functions = list(map(num_squrd,
                                   filter(num_even, list1)))
print(combined_list_functions)

row = int(input('Please Enter the number of rows'))
# Make diamond parttern with number of rows
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(end=' ')
    for j in range(1,2*i):
        print('*',end='')
    print()

# prompt user to input number and print fibonacci series till that number
# Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a,end=' ')
        a, b = b, a+b
    print()
fib(18)