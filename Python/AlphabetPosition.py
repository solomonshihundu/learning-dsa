from string import ascii_lowercase 
from string import ascii_uppercase

def position(char): 
    if char.islower():
        return "Position of alphabet: {0}".format( ascii_lowercase.index(char) + 1)
    else:
        return "Position of alphabet: {0}".format( ascii_uppercase.index(char) + 1)

def allPositions():
    for x in range (1,200):
        print(chr(x),end=" ")

def getUnicode(char):
    print(ord(char))

#print(position('A'))
#print(position('a'))
#allPositions()
getUnicode('A')
getUnicode('Z')
getUnicode('a')
getUnicode('z')