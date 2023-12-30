"""
Problem: Write a program that prompts for the names of a source file to read and a target file to write, and copy the
content of the source file to the target file, but with all empty lines removed, then output the number of
empty lines removed.
"""
import os
source = "Data_Files" + os.sep + input("Enter the name of the source file: ")
target = "Data_Files" + os.sep + input("Enter the name of the target file: ")
with open(source, "r") as f:
    with open(target, 'w') as f1:
        lines = f.readlines()
        empty_lines = 0
        # Iterate over the lines
        for line in lines:
            if line == "\n":
                empty_lines += 1
            else:
                f1.write(line)
        print(f'Number of lines remoed {empty_lines}')
