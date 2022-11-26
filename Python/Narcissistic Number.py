def narcissistic(value):
    str_value = str(value)
    result = 0

    power = len(str_value)
    # print(power)

    for i in iter(str_value):
        #print(i,end=" ")
        result += pow(int(i),power)

    if result == value:
        return True
    return False    


#153 True
#371 True
#1234 False
num = 1234
print(narcissistic(num))

#################################################################################################
# BEST PRACTISE
#################################################################################################
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
