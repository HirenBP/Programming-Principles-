"""
Problem: Given starting and ending years, write a program with a function to calculate the number of days from starting
 year to ending year inclusive.  Hints: Write a function to check leap year. Sample code is in the lecture notes of
 Section 10: Type Bool and Boolean Expressions. Sample run:
Year 1? 1980
Year 2? 2022
Number of days: 15706

"""
# Function to calculate number of days between years.
def calc_days(y1, y2):
    # Variable to keep track of leap years.
    ly =0
    #Years because years are inclusive with need to add 1 to equations
    years = (y2 - y1) + 1
    # Range function goes from 2022 to before 1980 to fix that we need to add -1 so that it will stop before 1979
    for i in range(y2,y1-1,-1):
        # If value of i (which is a year in range) is divisible by 4 it is a leap year
        if i % 4 == 0:
            # Increase the counter of leap year.
            ly += 1
    # Return number of days. Year * 365 plus day each for leap years
    return (years * 365) + ly
year1 = int(input('Year 1? '))
year2 = int(input('Year 2? '))
print(f'Number of days : {calc_days(year1,year2)}')