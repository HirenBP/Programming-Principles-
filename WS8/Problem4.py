"""
Problem4: Given two lists, write a program with a function that merges these two lists in descending order.
Your main program willl allows the user to enter two lists of numbers and end the program by inputting a blank
line for list1. You are not allowed to concatenate the two lists into a new list and then ccall the built in
sort function. But you are allowed to sort the two lists in descending order before merge. Don't worry about
the complexity of the merging alogrithm
"""

def merge(list1, list2):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result




input1 = input('List 1: ')
while input1 != '':
    input2 = input('List 2: ')
    l1 = [int(x) for x in input1.split()]
    l2 = [int(x) for x in input2.split()]
    print(merge(l1,l2))
    input1 = input('List 1: ')