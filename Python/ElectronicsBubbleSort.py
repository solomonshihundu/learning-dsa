from Decorators import time_it

class Bubble:

    #Constructor initializes the data
    def __init__ (self,data):
        self.data = data

    @time_it
    def sort_data(self,key):
        #Store the data in local variable
        data_set = self.data
        output = []

        #Get the length of the data set to limit the for loop
        size = len(data_set)

        for i in range(size-1):
            swapped = False
            for j in range (size-1-i):
                a = data_set[j][key]
                b = data_set[j+1][key]

                if a > b: 
                    tmp = data_set[j]
                    data_set[j] = data_set[j+1]
                    data_set[j+1] = tmp
                    swapped = True

            if not swapped:
                break      
            
        #Return the sorted version
        return data_set

    def print_data(self,data_list):
        for i in data_list:
            print(i,end="\n")
        

def test_bubble_sort():
    #Generate test data
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    
    #Pass test data into class constructor
    test = Bubble(elements)
    
    #return the class object
    return test

if __name__ == '__main__':
    data = test_bubble_sort().sort_data(key="transaction_amount")
    test_bubble_sort().print_data(data)
    data = test_bubble_sort().sort_data(key="name")
    test_bubble_sort().print_data(data)
