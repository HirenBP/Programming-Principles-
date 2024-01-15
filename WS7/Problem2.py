"""
Problem: Write a Python program that prompts for the name of a file, then prints the frist two
lines and the last two lines of the file
"""

source = '\\'.join(['Data_Files',input('Enter file name :')])
with open(source) as file1:
    lines = file1.readlines()
    for num,line in enumerate(lines):
        if num < 2:
            print(line.strip())
        if num > len(lines)-3:
            print(line.strip())


