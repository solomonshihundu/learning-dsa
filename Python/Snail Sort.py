def snail(snail_map):
    output = []

    while snail_map:
    
        #First Row
        for i in snail_map[0]:
            output.append(i)
        snail_map.pop(0)

        if not snail_map:
            break

        #Second Row
        for j in snail_map:
            output.append(j[-1])
            j.pop()

        #Last Row
        for K in range(len(snail_map[-1]) -1,-1,-1):
            output.append(snail_map[-1][K])
        snail_map.pop()

        if not snail_map:
            break

        #Moving upwards
        for l in reversed(snail_map):
            output.append((l[0]))
            l.pop(0)

    return output
 

###########################################################################################################
# BEST PRACTISE
###########################################################################################################

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


def snail_two(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


array_two = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail_two(array_two))