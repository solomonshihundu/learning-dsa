# method to locate our cards
def locate_card(cards, query):
    
    # create a varible inital position at zero
    position = 0
    
    # loop through our set of cards
    while position < len(cards):
        #if the card in the initial position is our card, return the position and exit loop
        if cards[position] == query:
            return position
        
        #if its not the increase the position by 1 and continue the loop
        else:
            position += 1
    # if we have reached the end of our deck of cards 
    # card was not found in deck
    return -1

# define inputs
cards = [18, 14, 12, 11, 7, 5, 3, 1]
query = 7

# call method
result = locate_card(cards,query)
print(result)

# def test(self,locate_card,test):
#     self.assertEqual(1, 0, "broken")

# ############# TEST CASES ############
# # 0 General Case
# test = {
#     'input' : {
#         'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
#         'query': 1
#         },
#         'output' : 6
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 1 The number query occurs somewhere in the middle of the list cards.
# test = {
#     'input' : {
#         'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
#         'query': 1
#         },
#         'output' : 6
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 2 query is the first element in cards.
# test = {
#     'input' : {
#         'cards' : [4, 2, 1, -1],
#         'query': 4
#         },
#         'output' : 0
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 3 query is the last element in cards.
# test = {
#     'input' : {
#         'cards' : [3, -1, -9, -127],
#         'query': -127
#         },
#         'output' : 3
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 4 The list cards contains just one element, which is query.
# test = {
#     'input' : {
#         'cards' : [ 6],
#         'query': [6]
#         },
#         'output' : 0
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 5 The list cards does not contain number query.
# test = {
#     'input' : {
#         'cards' : [9, 7, 5, 2, -9],
#         'query': 4
#         },
#         'output' : -1
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 6 The list cards is empty.
# test = {
#     'input' : {
#         'cards' : [],
#         'query': 7
#         },
#         'output' : -1
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 7 The list cards contains repeating numbers.
# test = {
#     'input' : {
#         'cards' : [ 19, 18,14, 14, 11, 11, 8, 8, 5, 3, 3, 1],
#         'query': 5
#         },
#         'output' : 8
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)

# # 8 The number query occurs at more than one position in cards.
# test = {
#     'input' : {
#         'cards' : [ 19, 18, 14, 11, 11, 8, 7, 7, 7, 5, 3, 3, 1],
#         'query': 7
#         },
#         'output' : 6
# }

# # run test case
# result = locate_card(**test['input']) == test['output']
# print(result)