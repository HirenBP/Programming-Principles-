# celiFloor1.py
# use the ceil and floor from the math module qualified
# Ceil method rounds number up to positive infinity
# Floor method rounds the number down to negative infinity.
# There are multiple ways to import module
# import math - this on you'll have to qualify the ceil and floor method by adding math. before calling the method.
# fromm math import ceil,floor - this one only imports ceil and floor methods from math module. You can use the
# ceil and floor without qualifying it.
from math import *  # this imports all methods from math module, and you don't have to use qualifying names.

x = 10 / 3
print("x = {:.4f}".format(x))
print("Ceil (x) = {:.4f}".format(ceil(x)))
print("floor(x) = {:.4f}".format(floor(x)))
