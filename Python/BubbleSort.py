from DataGenerator import Generator
from Decorators import time_it

class Bubble:

    #Constructor initializes the data
    def __init__ (self,data):
        self.data = data

    @time_it
    def sort_data(self):
        #Store the data in local variable
        data_set = self.data

        #Get the length of the data set to limit the for loop
        size = len(data_set)
        
        #Outter loop ensures we run this process as many times as needed
        #while is until all elements in the loop are sorted
        for i in range(size - 1):
            #The swapped var is set to true only if a swap occurs
            #in the case that a swap doen't take place, meaning we now
            #have a sorted list , we then break from the code
            #making the code more efficient
            #sort_data took 3455.7931423187256 mille seconds
            #sort_data took 1.009225845336914 mille seconds
            swapped = False
            #While looping through the elements its logical not to perform a
            #loop through the very last element since by that point the right part of the list is
            #already sorted
            for j in range(size - 1 - i):
                #Perform the classic swap
                if data_set[j] > data_set[j+1]: 
                    tmp = data_set[j]
                    data_set[j] = data_set[j+1]
                    data_set[j+1] = tmp
                    swapped = True
            if not swapped:
                break
        #We Return the sorted version of the list
        return data_set

    def print_data(self,data_list):
        for i in data_list:
            print(i,end=" ")
        

def test_bubble_sort():
    #Generate test data
    test_data = Generator(1,1000).generate_data("EVEN")
    
    #Pass test data into class constructor
    test = Bubble(test_data)
    
    #return the class object
    return test

if __name__ == '__main__':
    data = test_bubble_sort().sort_data()
    test_bubble_sort().print_data(data)
