# Problem4.py
# Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours.
# Only whole hours are counted. If he works more hours than that (overtime) he gets paid at 1.5 times
# his normal rate for the overtime. If he sells more than 5 cars in a week, he gets a bonus of $200 per car
# from the 6th car sold. Write a program that takes as input the number of hours worked and the total
# number of cars sold for the week, and outputs the car dealer’s total salary for the week.
hours_worked = int(input("Enter the number of hours worked: "))
cars_sold = int(input("Enter the total number of cars sold: "))
if hours_worked <= 37:
    base_pay = hours_worked * 36.25
else:
    base_pay = 37 * 36.25 + (hours_worked - 37) * 54.375
if cars_sold > 5:
    bonus = (cars_sold - 5) * 200
else:
    bonus = 0
total_pay = base_pay + bonus
print("The salary is ", total_pay)
