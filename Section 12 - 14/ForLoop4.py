# Marks.py
# Prompt for the number of marks and read them
# Print the number of marks entered and the
# average (arithmetic mean) of the marks.

n = int(input('How many marks: '))
if n > 0:
    mark = float(input('Please enter a mark : '))
    highest = mark
    lowest = mark
    total = mark
    for i in range(n - 1):
        mark = float(input('Please enter a mark : '))
        total += mark
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    print('The number of marks: ', n)
    print('The average mark is ', total / n)
    print('The lowest mark is ', lowest)
    print('The highest mark is ', highest)

# When you initialize variable think about the first value the variable should have instead of making the values up.
