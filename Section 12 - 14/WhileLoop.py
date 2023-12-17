# Marks.py
# Prompt for and read marks for a test until a negative number is entered
#(which can not be a valid mark). Print the number of marks entred and the
# average (arithmetic mean) of the marks.
n = 0
total = 0.0
mark = float(input('Please enter a mark : '))
highest = mark
lowest = mark
while mark >= 0:
    n += 1
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    mark = float(input('Please enter a mark : '))
print('The number of marks: ', n)
if n > 0:
    print('The average mark is ', total / n)
    print('The lowest mark is ', lowest)
    print('The highest mark is ', highest)

# When you initialize variable think about the first value the variable should have instead of making the values up.
# 