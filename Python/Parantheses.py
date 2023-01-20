def valid_parentheses(string):
    
    #Storers all parentheses from input string
    para = []

    #List that serves as our stack
    stack = []

    #Dictionary defining open parentheses as Key
    # and closing parentheses as Value
    para_dict = {'(':')'}
    
    #loop through string check if string has : '(' and ')'
    # Add only parentheses to the list
    for x in string:
        if x == "(" or x ==")":
            para.append(x)
    
    #Loop through the parentheses list
    for char in para:
        
        #If the parentheses is an openning
        #Add it to the stack list
        if char in para_dict.keys():
            stack.append(char)
        
        else:
            #if the stack list is empty return false
            #else remove the last elemnt in the list
            if stack == []:
                return False
            open_brac = stack.pop()

            if char != para_dict[open_brac]:
                return False
    
    #if the stack list is never altered
    #it remains empty thus return true in the end
    return stack == []


input = "())(" #"hi(hi)()" #"())("  # ())(
#input = "hi(hi)()"

print(valid_parentheses(input))
###################################################################################
#BEST PRACTISE ONE
###################################################################################

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

###################################################################################
#BEST PRACTISE ONE
###################################################################################
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0