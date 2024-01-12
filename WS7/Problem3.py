"""
Problem3: Write a program that prompts for the name of a file containing number in each line, prints
the average of each line. Assume each line contain numbers only and they are separated by a space.
"""
import os
source = '\\'.join(['Data_Files',input('File name :')])
with open(source) as file1:
    line_avg = []
    counter = 1
    lines = file1.readlines()
    for line in lines:
        numbers = [int(i) for i in line.split(" ")]
        average = sum(numbers) / len(numbers)
        line_avg.append(average)
    for avg in line_avg:
        print(f'The average of line {counter} is {avg}')
        counter += 1