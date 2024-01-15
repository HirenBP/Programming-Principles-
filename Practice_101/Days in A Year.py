import datetime

# Define a function that takes two years as arguments and returns the number of days between them
def days_between_years(year1, year2):
    # Create a date object for the first day of the first year
    date1 = datetime.date(year1, 1, 1)
    # Create a date object for the last day of the second year
    date2 = datetime.date(year2, 12, 31)
    # Calculate the difference between the two dates and get the number of days
    difference = date2 - date1
    return difference.days

# Test the function with some examples
print(days_between_years(1980, 2022)) # Output: 12418)
print(days_between_years(1988, 2021)) # Output: 12418
print(days_between_years(1978, 2008)) # Output:
