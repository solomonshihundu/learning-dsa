def count_sheeps(sheep):
    count = 0
    if sheep == []:
        return 0

    for x in sheep:
        if type(x) == bool and x == True:
            count += 1
        
    return count

sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
print(count_sheeps(sheep))



#################################################################################################
# BEST PRACTISE
#################################################################################################
def count_sheeps(sheep):
  return sheep.count(True)

