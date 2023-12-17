# Problem 1 requires us to calculate Liters of concerete require for a park.
# We will create a function then as for inputs lenght, width and litres per sqm from user
# Function will calculate the litres of concrete required to fill the park floor.
# Print the return value to console
def cacl_area(len, wid, liter):
    return len * wid * liter
lenght = float(input('Lenght of park (m): '))
width = float(input('Width of park (m): '))
liters_per_sqm = float(input('Liters per squire meter : '))

print(f'Liters required = {cacl_area(lenght, width, liters_per_sqm)}')
