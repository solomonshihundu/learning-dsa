from Decorators import time_it
from DataGenerator import Generator

#Search class defines the binary and linear search class functions
class Search:
    def __init__ (self, data_set):
        self.data_set = data_set
        self.value = None
        self.index = None
        self.search_type = None

    @time_it
    def linear_search(self,value):
        self.value = value
        self.search_type = "Linear Search"
        for index, element in enumerate(self.data_set):
            if element == value:
                self.index = index
                self.print_result()
        print("Value not found")
        self.index = -1
        return -1

    @time_it
    def binary_search_iterative(self,value):
        self.value = value
        self.search_type = "Binary Search Iterative"

        left_index = 0
        right_index = len(self.data_set) - 1
        mid_index = 0

        while left_index <= right_index:
            mid_index = (right_index + left_index) // 2
            mid_point = self.data_set[mid_index]

            if mid_point == self.value:
                self.value = value
                self.index = mid_index
                self.print_result()

            if mid_point < value:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        print("Value not found")
        return -1

    #@time_it
    def binary_search_recursive(self,value,left_index,right_index):
        self.value = value
        self.search_type = "Binary Search Recursive"

        if right_index < left_index:
            return -1

        mid_index = (left_index + right_index) // 2
        mid_point = self.data_set[mid_index]

        if mid_point == value:
            self.value = value
            self.index = mid_index
            return (self.index,self.value)
        
        if mid_point < value:
                left_index = mid_index + 1
        else:
            right_index = mid_index - 1

        self.binary_search_recursive(value,left_index,right_index)
       

            
    def print_result(self):
        print(self.search_type + f" : The number {self.value} is at index {self.index}")



if __name__ == '__main__': 

    #Test Data
    gen = Generator(1,1000000)
    num_list = gen.generate_data("ODD")

    search = Search(num_list)

    search.linear_search(4)
    search.binary_search_iterative(4)
    rec_result = search.binary_search_recursive(4,0,(len(num_list)))
    print(rec_result)
   

