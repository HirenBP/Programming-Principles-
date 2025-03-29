"""
A store pays its entry-level employees weekly salary based on their ages and length of contract in months if the age is 20:

Age	Weekly Salary
14-15	343.44
16-17	457.92
18-19	610.56
20, 6 months or less contract	686.88
20, longer than 6 months contract	763.20
>20	850.34


Write a program that reads the age and length of the contract for an employee, and then prints the equivalent annual salary of the employee. (Assume 52 weeks per year.)



Example:

Age: 20

Contract length: 8

Annual salary: 39686.4
"""

# Function to get yearly salary
def get_weekly_salary(age, len_contract):

        if 14 <= age <= 15:
            return 343.44
        elif 16 <= age <= 17:
            return 457.92
        elif 18 <= age <= 19:
            return 610.56
        elif age == 20:
            if len_contract <= 6:
                return 686.88
            else:
                return 763.20
        elif age > 20:
            return 850.34
        else:
            return "Invalid age provided"

# Ask the user to enter the Age and Lenght of the contract
user_age = int(input("Age:"))
contract_len = int(input("Contract lenght:"))

#Print Annual Salary
print(f'Annual salary: {get_weekly_salary(user_age, contract_len)*52}')


