f = open('input.txt')

import numpy as np



def partOne():
    correctStrings = 0
    array = f.readlines()
    tokens = ['a','e','i','o','u']
    tokensCoupple = ['ab','cd','pq','xy']
    for object in array:
        vowels = 0
        appears = 0
        string = True
        for i in range(len(object)-1):
            if(object[i] in tokens):
                vowels += 1
            if(object[i] == object[i+1]):
                appears += 1
            if((object[i] + object[i+1]) in tokensCoupple):
                string = False

        if vowels >= 3 and appears >= 1 and string:
            correctStrings += 1
    print(correctStrings)



    
partOne()



