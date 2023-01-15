import os
from turtle import position

from numpy import number

f = open('day1/input.txt')

counter = 0
position = 0
numbers = [n for n in f.readlines()]
characters = list(numbers[0])

for i in characters:
    print(i)
    if( i == '('):
        counter += 1
    else:
        counter -= 1
    position += 1
    if(counter == -1):
        break

    

print(counter)
print(position)