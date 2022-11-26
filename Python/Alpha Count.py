def count(string):
    result = {}

    for x in string:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1

    return result

input = "ApPles fOr the DoctOr"
print(count(input))

#################################################################################################
# BEST PRACTISEs
#################################################################################################

from collections import Counter

def count(string):
    return Counter(string)


def count(string):
  
    return {i: string.count(i) for i in string}