"""
Write a function called mytest(chars,option) to check wheter string chars meets certain conditions or not then
return True or False.
"""
def mytest(chars, option = 'aplpha'):
    if option == 'aplpha':
        for char in chars:
            if char.isalpha():
                return True
            else:
                return False

    elif option == 'digit':
        for dig in chars:

            if dig.isdigit():
                    return True
            else:
                    return False
    elif option == 'space':
        for space in chars:
            if space.isspace():
                return True
            else:
                return False
