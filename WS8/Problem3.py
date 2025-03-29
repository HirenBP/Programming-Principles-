"""
Problem: Write a program with a function that given a list of numbers, returns True if and only if all of the numbers
 in the list form an arithmetic progression, that is the difference between any two successive numbers in the list is
  the same. Your main program should read a file containing space-separated numbers as test lists, print each list and
  the outcome after calling the function.
"""

def isArithmeticProgression(list):
    result = None
    if len(list) < 2:
        result = False
    diff = list[0] - list[1]
    for i in range(1,len(list)-1):
            temp = list[i] - list[i + 1]
            if temp == diff:
                result = True
            else:
                result = False
    return result

source = "//".join(['Data_Files', input('File Name: ')])
with open(source,'r') as f:
    lines = f.readlines()
    for line in lines:
        list = [int(x) for x in line.split()]
        print(list,end=' ')
        print(isArithmeticProgression(list))
