# The grades at a university are awarded based on the marks awarded for the course out of
# 100. Marks of 85 or above receive the grade of 7. Marks less than 85 but that are 75 or above receive
# the grade of 6. Marks less than 75 but that are 65 or above receive the grade of 5. Marks less than 65
# but that are 50 or above receive the grade of 4. Anything less than 50 gets the grade of F. Write a
# program that asks the user to input the marks and prints the grade awarded.
# def calc_grade(m):
#     if m < 50:
#         return 'FAIL'
#     elif 50 <= m < 65:
#         return 4
#     elif 65 <= m < 75:
#         return 5
#     elif 75 <= m < 85:
#         return 6
#     elif m >= 85:
#         return 7
# mark = float(input("How many marks ? "))
# print(f'Grade awarded: {calc_grade(mark)}')
mark = float(input("How many marks ? "))
grade = 7 if mark >= 85 else 6 if mark >= 75 else 5 if mark >= 65 else 4 if mark >= 50 else "F"
print(f'Grade awarded: {grade}')