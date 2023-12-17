# To print reverse triangle
#####
####
###
##
#
rows = int(input("Please enter number of rows"))
b = 0
#reverse loop iteration starts from rows to 0 and use -1 in range function
for i in range(rows,0,-1):
    b+= 1
    for j in range(1,i + 1):
        print(b,end='')
    print()

# with same digit or * pattern
for h in range(rows,0,-1):
    for k in range(1,h+1):
        print('*',end='')
    print()