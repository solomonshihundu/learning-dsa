import time
from DataGenerator import Generator

#Search class defines the binary and linear search class functions
class Search:
    def __init__ (self, data_set):
        self.data_set = data_set
        self.value = None
        self.index = None
        self.search_type = None

    def linear_search(self,value):
        self.value = value
        self.search_type = "Linear Search"
        for index, element in enumerate(self.data_set):
            if element == value:
                self.index = index
                self.print_result()
        self.index = -1

    def binary_search(self,value):
        self.value = value
        self.search_type = "Binary Search"

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

        return -1

    def print_result(self):
        print(self.search_type + f" : The number {self.value} is at index {self.index}")


def perform_search():
    
    #Test Data
    gen = Generator(1,1000000)
    num_list = gen.generate_data()
    
    search = Search(num_list)
    return search


if __name__ == '__main__': 

    test = perform_search()
    
    st_time = time.time()
    test.linear_search(999999)
    end_time = time.time()
    tt = end_time - st_time
    print(f"Time Taken : {tt} ms")

    st_time = time.time()
    test.binary_search(999999)
    end_time = time.time()
    tt = end_time - st_time
    print(f"Time Taken : {tt} ms")


