# To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a
# triangular pattern.
"""
The pascals triangle looks like this
1
11
121
1331
14641
15101051
1615201561
"""
def print_pascal_triangle(size):
    # 0 to size loop
    for i in range(0,size):
        for j in range(0,i+1):
            print(decide_number(i,j),end=' ')
        print()
def decide_number(n,k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0,k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

rows = int(input('Enter number of rows'))
print_pascal_triangle(rows)