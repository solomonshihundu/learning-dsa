def array_diff(a, b):
    i = 0
    while i <= len(a):
        for x in a:
            if x in b:
                a.remove(x)
        i += 1

    return a

l1 = [1,2,3,3,4,5,9,10,11,12]
l2 = [1,3,6,7,8,10,11,13,14]

print(array_diff(l1,l2))

#################################################################################################
# BEST PRACTISE
#################################################################################################
def array_diff(a, b):
    return [x for x in a if x not in b]