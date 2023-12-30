"""
Problem: Write a Python program that prompts for the name of a file, then prints the frist two
lines and the last two lines of the file
"""

source = '\\'.join(['Data_Files',input('Enter file name :')])
with open(source) as file1:
    lines = file1.readlines()
print(*lines[0:2])
print(*lines[-2:])


