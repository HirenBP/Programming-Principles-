import re
s1 = input('String:')
match = re.findall(r'gg', s1)
print('IsHappy?:', len(match) > 0)