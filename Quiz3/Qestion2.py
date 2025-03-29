"""
Write a program that prompts for the name of the file to read, then count and print the number of words
that contain only lowercase letters.
"""
source = input('Enter the name of the source file: ')
with open(source, 'r') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            temp = line.split()
            for t in temp:
                if t.islower():
                    words.append(t)
        print(f'Number of words that has only lower case letters are : {len(words)}')
