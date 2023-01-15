f = open('day3/input.txt')
import numpy as np


def partOne():
    array = np.zeros((1000,1000))
    x = 500
    y = 500
    array[500,500] = 1
    tokens= {'^': (0,1),'v': (0,-1),'>': (1,0),'<': (-1,0)}
    for i in f.read().strip():
        directionx, directiony = tokens[i]
        x += directionx
        y += directiony
        array[x,y] = 1
    print(np.count_nonzero(array))



def partTwo():
    array = np.zeros((1000,1000))
    x = 500
    y = 500
    xx = 500
    yy = 500
    array[500,500] = 1
    tokens= {'^': (0,1),'v': (0,-1),'>': (1,0),'<': (-1,0)}
    array_tokens = f.readline()
    for i in range(0,len(array_tokens)):
        if(i % 2 == 0):
            directionx, directiony = tokens[array_tokens[i]]
            x += directionx
            y += directiony
            array[x,y] = 1
        else:
            directionx, directiony = tokens[array_tokens[i]]
            xx += directionx
            yy += directiony
            array[xx,yy] = 1
    print(np.count_nonzero(array))
partTwo()