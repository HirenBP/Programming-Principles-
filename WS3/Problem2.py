# Problem 2.py
# Problem: A shipping company charges its customer based on the weight of goods and the distance of
# shipping. A discount is given based on the distance of shipping as follows:
# distance < 250km, no discount
# 250km ≤ distance < 500km, 10% discount
# 500km ≤ distance < 1000km, 15% discount
# 1000km ≤ distance < 2000km, 20% discount
# 2000km ≤ distance < 3000km, 35% discount
# 3000km ≤ distance, 50% discount
# The shipping cost is calculated based on the following equation:
# cost = base price * weight * distance * (1 - discount).
# Write a program that takes as inputs the base price, weight, and distance, and prints the shipping cost to be
# charged to the customer.


baseprice = float(input('How much is the base price? '))
weight = float(input('What is the weight? '))
distance = float(input('What is the distance? '))
discount = 50 if distance >= 3000 else 35 if distance >= 2000 else 20 if distance >= 1000 \
    else 15 if distance >= 500 else 10 if distance >= 250 else 0
if discount > 0:
    print(f'Shipping cost is {baseprice * weight * distance * (1 - (discount / 100))}')
else:
    print(f'Shipping cost is {baseprice * weight * distance}')

