"""
Problem: Write a program that allows the user to enter the marks of 5 students in 4 courses, and outputs
the highest average marks for students and courses. Hint: Consider 2 dimensional lists,
 i.e. the element of a list is a list.
"""
# Initialize two-dimensional list (list of lists)
marks = []
# Get user input and store input in a list mark
# append list mark to two-dimensional list marks
for i in range(1, 6):
    s1 = input(f'Student {i} (courses 1-4):')
    mark = [int(j) for j in s1.split()]
    marks.append(mark)
# Function to get average of items in list
def average(lst):
    return sum(lst) / len(lst)
# Function to get the highest average of list from two-dimensional lists.
def hightest_average(lst):
    return max(average(sublist) for sublist in lst)
# Function to transpose two-dimensional list so that list of students and marks
# becomes list of course and marks
def transpose(lst):
    return [list(row) for row in zip(*lst)]
# Print values returned by functions
print('The highest average mark of students: ', hightest_average(marks))
print('The highest average mark of courses: ', hightest_average(transpose(marks)))