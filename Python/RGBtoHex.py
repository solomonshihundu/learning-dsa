def rgb(r,g,b):
    
    #Insert inputs into iterable list
    input = [r,g,b]

    #String to store final output
    output = ""

    #Iterable list to store our hex converted input
    hex_list = []

    #lopp through the input list 
    for x in input:
        #If the value is a negavive set it to zero
        if x < 0:
            x = 0
        #If the value is out of bounds set it to max : 255
        if x > 255:
            x = 255
        #If the value results to a single digit Hez i.e 0,1,2 .... D,E,F
        #Take the last value in string and append a leading zero i.e 00,01,02 ... 0D,0E,0F
        #Append value to output string
        if x < 15:
            #Convert to upper case
            temp = hex(x).upper()
            temp = temp[-1:]
            hex_list.append(str(temp).zfill(2))    
        #If the value is a two digit hex i.e 10,11,1D,4G ...
        #Take the last two values from the string
        #Append to output
        else:
            temp = hex(x).upper()
            temp = temp[-2:]
            hex_list.append(temp)
                

    for i in hex_list:
        output += i
            
    return output

#TEST DATA
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))

########################################################################################################
#BEST PRACTISE
########################################################################################################

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))



def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
