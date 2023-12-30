"""
Find largets element in array for given array of ineger.
"""
def largestnumber(numbers):
    biggest_number = numbers[0]
    for num in numbers:
        if num > biggest_number:
            biggest_number = num
    return biggest_number

def smallest_number(numbers):
    smaleest_number = numbers[0]
    for num in numbers:
        if smaleest_number > num:
            smaleest_number = num
    return smaleest_number

print(largestnumber([100,345,234,465,456,234,234,563,45234234,4546,3,534]))
print(smallest_number([100,345,234,465,456,234,234,563,45234234,4546,3,534]))



