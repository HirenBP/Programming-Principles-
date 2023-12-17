def reverse_string_recursive(string):
    restring=''
    if len(string) == 0:
        return ""
    else:
        restring = reverse_string_recursive()
    return reverse_string_recursive(string[1:]) + string[0]
s1 = 'Modules and Workshops World !'
print(s1)
reversed_string = reverse_string_recursive(s1)
print(reversed_string)