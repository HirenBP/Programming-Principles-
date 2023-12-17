#week 7 additional questions

#question 1
# Write a Python program that reads an integer that
# gives the number of integers to be read, and then reads these integers
# into a list. Print the total of these integers except that if an integer
# appears more than once it will only be counted once.
# For example, the input:
#   5 1 2 3 4 5 would give 15
#   5 1 2 3 4 2 would give 10
#   5 1 2 1 4 2 would give 7

num = int(input('Please enter the number of integers to read'))

def readtolist():
    return [int(input('Enter number'+str(i+1)+':')) for i in range(num)]
def deduplicate(L):
    L1 = []
    for x in L:
        if x not in L1:
            L1.append(x)
    return L1
li = readtolist()
print(li,sum(deduplicate(li)))
