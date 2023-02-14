#Sort method takes two args, the data and a key defaulted to 'First Name' if not given
#The key determines the sorting options, either by First Name or Last Name
def selection_sort(data,key='First Name'):
    
    #Get size of list to limit iteration
    size = len(data)
    
    #Outter loop traverses the list 
    for element in range(size-1):
        
        #Define the initial minimum value as the first element of our list
        min_index = element

        #Staring with the second element on the list we determine if the its 
        #alphabetically less than the initially defined min value, where a < b < c... < z 
        #Python considers the first character of the string, if so then its set as the
        #min value index
        for j in range(min_index + 1, size):
            if data[j][key] < data[min_index][key]:
                min_index = j
        
        #As long as the current element in the outter loop is not the min element 
        # we perform as swap between the current element and min value, this goes
        #leftwards until the min value index is on the far left with every iteration
        #sorting our list
        if element != min_index:
            data[element],data[min_index] = data[min_index],data[element]

if __name__ == '__main__':
    
    #Initialize test data
    data_set = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    selection_sort(data_set,'Last Name')

    for i in data_set:
        print(i)