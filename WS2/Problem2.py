# def calc_wage(hours, days, annual):
#     hours_worked_week = hours * days
#     return  annual / (hours_worked_week * 52)
# num_hours = float(input('Number of hourse worked per day: '))
# num_days = float(input('Number of days worked in a week :'))
# annual_salary = float(input('Annual salary:'))
#
# print(f'Hourly wage = {calc_wage(num_hours,num_days,annual_salary)}')
def calc_wage(hours, days, annual):
    hours_worked_week = hours * days
    return  annual / (hours_worked_week * 52)
num_hours = float(input('Number of hours worked per day: '))
num_days = float(input('Number of days worked in a week :'))
annual_salary = float(input('Annual salary:'))
print(f'Hourly wage = {calc_wage(num_hours,num_days,annual_salary)}')
