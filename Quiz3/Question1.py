
"""
Write a program that prompts for the names of a source file to read and a target file to write,
and copy the content of the source file to the target file
, but with all lines containing the colon symbol ‘:’ removed. Finally, close the files.
"""
source = input('Enter the name of the source file: ')
target = input('Enter the name of the target file: ')
f = open(source, 'r')
f1 = open(target, 'w')
lines = f.readlines()
for line in lines:
    if ';' not in line:
        f1.write(line)
f.close()
f1.close()