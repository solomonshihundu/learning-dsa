def get_middle(s):

    charCount = int(len(s))

    #Char count is Even
    #Trio   : ri
    if charCount % 2 == 0:
        index = (int(len(s)/2) - 1)
        print(s[index:index+2])
    else:
        #Char count is Odd
        #Solomon  : o
        index = (int(len(s)/2))
        print(s[index])

get_middle("Trio")
###################################################################################
#BEST PRACTISE ONE
###################################################################################

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]