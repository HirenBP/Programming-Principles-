"""
Write a function that accepts two arguments, an integer, d, and a list of integers, and returns True if and only if
no pair of different elements selected from the list differ by less than d, otherwise, return False.
For example, given a list [4, 500, 1, 6, 30], if d is 3 then return False, since 6 - 4 < 3; if d is 2, then return True.
"""
# def check_difference(d, list):
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if abs(list[i] - list[j]) < d:
#                 return False
#     return True
def no_pairs_differ_by_less_than_d(d, list_of_ints):

    list_of_ints.sort()  # Sort the list to efficiently compare adjacent elements

    for i in range(len(list_of_ints) - 1):
        if list_of_ints[i + 1] - list_of_ints[i] < d:
            return False

    return True
d = 3
list = [4,500,1,6,30]
print(no_pairs_differ_by_less_than_d(d, list))
