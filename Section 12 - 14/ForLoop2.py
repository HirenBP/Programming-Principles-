# Problem2: Prompt for and read number of rows and columns. Print those many rows and columns of hashes.

rows = int(input("Please entre number of rows : "))
column = int(input('Please enter number of columns : '))

for i in range(rows): # range of integer is enumerable
    for j in range(column):
        print('#', end='')
    print()



