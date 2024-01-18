"""
Problem: Given two lists, write a program with a function that takes these two lists as the input arguments and returns
 the list of all the elements in the first list that occur in the second list. The returned list shall not contain
 duplicate elements.Your main program will allow the user to enter two lists of numbers and end the program by
 inputting a blank line for list 1.
"""

def find_common_elements(list1, list2):
    temp = set()
    for i in list1:
        if i in list2:
            temp.add(i)
    return temp

input1 = input('Enter list1: ')
while input1 != '':
    input2 = input('Enter list2: ')
    l1 = [int(x) for x in input1.split()]
    l2 = [int(x) for x in input2.split()]
    print([*find_common_elements(l1,l2)])
    input1 = input('Enter list1: ')
