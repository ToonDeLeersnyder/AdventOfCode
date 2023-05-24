import hashlib
import numpy as np


def partOne():
    number  = 0
    sumof = 0
    while(1):
        source = 'bgvyzdsv{0}'.format(number).encode()
        arrayHash = hashlib.md5(source).hexdigest()
        
        array = np.array((arrayHash[0:5]))
        if(array == '00000'):
            break
        number += 1
    print(sumof)
    print(number)
    



def partTwo():
    number  = 0
    sumof = 0
    while(1):
        source = 'bgvyzdsv{0}'.format(number).encode()
        arrayHash = hashlib.md5(source).hexdigest()
        
        array = np.array((arrayHash[0:6]))
        if(array == '000000'):
            break
        number += 1
    print(sumof)
    print(number)

partOne()
partTwo()