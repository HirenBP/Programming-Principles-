# Print Inverted Triangle
#     1
#    12
#   123
#  1234
# 12345

rows = int(input('Please enter number of rows'))
for i in range(1,rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ",end=' ')
        else:
            print(num,end=' ')
            num += 1
    print()