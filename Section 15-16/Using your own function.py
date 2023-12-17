# Below and example of the simple function that takes no arguments and doesn't return anything
def printBoo():
    print('Boo !')


printBoo()
printBoo()
printBoo()


# Below example of the function that takes and argument
def printVertical(x):
    """ Printing X in verticle format """
    for c in str(x):
        print(c)


printVertical('Boo!')
printVertical('Modules and Workshops World !')


# Returning Values
# The return statement exits a functon, optionally returning a value
# Below function takes multiple arguments and returns a value
def finalBalance(p, r, n):
    """Returns a final balance with compound interest
    p in the principle (initial balance)
    r is the interest rate per term
    n is the number of terms"""
    return p * (1.0 + r) ** n
initBal = float(input("Initial balance: "))
annRatePct = float(input("Annual interest rate (%)"))
months = int(input("Number of months: "))
finalBal = finalBalance(initBal,annRatePct/ 100 / 12.0, months)
print('Final balance = ${:.2f}'.format(finalBal))