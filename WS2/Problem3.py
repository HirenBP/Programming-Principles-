# Problem: A primary school needs to arrange their students to sit for the National Assessment Program − Literacy and
# Numeracy test in multiple exam halls at Griffith University. Each school class has 25 students. A big exam hall can
# accommodate 45 students, and a small exam hall can accommodate 22 students. Write a program for the school to
# calculate
# how many full classes can be accommodated given the input numbers of big exam halls and small exam halls. For example,
# the program should look like this when run.
def calc_fullclass(big, small):
    available_space = (big * 45) + (small * 22)
    return available_space // 25
big_halls = int(input('How many big exam halls ? '))
small_halls = int(input('How many small exam halls ? '))
print(f'Number of classes = {calc_fullclass(big_halls, small_halls)}')
