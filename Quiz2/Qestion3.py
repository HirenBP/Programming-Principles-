rows = int(input('Number of rows: '))
for i in range(1,rows + 1):
    for j in range(rows, 0, -1):
        if j > i:
            print(" ",end=' ')
        else:
            print('*',end=' ')
    # Print new line at the end of outer loop.
    print()