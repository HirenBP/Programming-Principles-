# digits.py
# Print the number of characters in the string that are decimal digits.
n = 0
s = input('Enter a string : ')
for c in s:
    if '0' <= c <= '9':
        n += 1
print('Number of digits = ', n)