def valid_braces(string):
    
    #Define open and closing braces as key value pairs respectively
    braces_dict = {'{':'}','[':']','(':')'}

    #define an empty list to serve as out stack
    stack = []

    #loop through input string
    for char in string:

        #check if the element is a key in our braces dictionary
        if char in braces_dict.keys():
            
            #if present add it to the stack
            stack.append(char)
        else:

            #if the stack list is empty return false, statement is invalid as it has an initial close ')]}' without a preceeding open '([{'
            #else remove the last elemnt in the stack and return the element
            if stack == []:
                return False
            else:
                open_brace = stack.pop()

            #Check if the last element in the stack is an open '({[' that coinsides with the appropriate close ')]}'
            #if not the statement is invalid we return false
            if char != braces_dict[open_brace]:
                return False
            
            #We continue until end of loop

    #Once the loop has been exhausted 
    #if the stack is empty, then we return true as a;; pairs have been matched
    return stack == []

###################################################################################
# OTHER PRACTISES
###################################################################################

def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


def validBraces(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s
