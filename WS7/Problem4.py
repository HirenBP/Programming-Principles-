"""
Problem4: The Unit tool wc counts the number of characters, words and lines in a file. Write your own version of
wc that prompts for the name of the file ro tread, then prints the counts. Assume a word may contain letters, digits,
symbols and their mixture, but not space. Hyphenated words, e.g. large-scale are considered as a single word.
"""

import os
source = "Data_Files" + os.sep + input('File name:')
with open(source) as F1:
    lines = F1.readlines()
    words = []
    chars: int = 0
    for line in lines:
        temp = line.split()
        words.append(len(temp))
        chars = chars + len(line)
    print(f'Characters:{chars}')
    print(f'Words : {sum(words)}')
    print(f'Lines : {len(lines)}')