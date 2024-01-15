"""
Problem: Write a program with a function that given a list of numbers, rotate the numbers so the first number
becomes the last, and the rest of the numbers move one position forward. Do the rotation iteratively until the list
of numbers returns to its initial form.
"""

def swapList(l):
    temp = l[0]
    l = l[1:]
    l.append(temp)
    if l == my_list:
        print(l)
    else:
        print(l)
        swapList(l)
my_list = [int(x) for x in input('Input a list: ').split()]
print(my_list)
swapList(my_list)