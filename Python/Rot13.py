from string import ascii_lowercase 
#from string import maketrans

#rot13trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
#   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

def rot13(message):
    for x in message:
        #Check if char is an alphabet
        if x.isalpha():
            #Upper Case alphabet ranges from 65 - 90
            if x.upper():
                asciiIndex = ord(x)
            
        charIndex = 0
        output = ""
        if x.isalpha():
            asciiIndex = ord(x)
            #print(asciiIndex)
            newIndex = asciiIndex + 13
            newChar  = chr(newIndex)
            #print(newChar)
            output += newChar
        else:
            output += x

    print(output)

str = "OoohhH!"
rot13(str)

