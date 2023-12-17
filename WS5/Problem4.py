"""
Write a program that repeatedly asks the user for room dimensions until either dimension entered is zero.
For each room print the length and width (to the nearest millimetre), and the total length of carpet required in
 whole metres, to cover the room in two scenarios: lengthways manner and widthways manner. Hints: make good use
 of standard library functions; and simplify your program by writing a function to compute the total carpet length
  required given the room dimensions. Sample run:
"""
from math import ceil
def calculate_carpet_length(room_length, room_width, roll_width):
    # Calculate lengthways carpet needed
    lengthways = ceil(room_width / roll_width) * room_length

    widthways = ceil(room_length / roll_width) * room_width

    return round(lengthways), round(widthways)

roll_width = 3.66  # Roll carpet width in meters

while True:
    dim1 = float(input("Enter room dimension 1 (m): "))
    dim2 = float(input("Enter room dimension 2 (m): "))
    #Break condition
    if dim1 == 0 or dim2 == 0:
        break
    # Use of min and max functions
    room_length, room_width = max(dim1, dim2), min(dim1, dim2)
    lengthways, widthways = calculate_carpet_length(room_length, room_width, \
                                                    roll_width)

    print(f"Length of room = {room_length:.3f} m")
    print(f"Width of room = {room_width:.3f} m")
    print(f"Total carpet length required in lengthways manner = {lengthways} m")
    print(f"Total carpet length required in widthways manner = {widthways} m")
    print()
