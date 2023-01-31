class Occurance:
    #Class constuctor initializes the data passed 
    # together with the value and index
    def __init__(self,data):
        self.data = data
        self.value = None
        self.index = None

    #Fuction performs a binary search of the value passed
    def perform_search(self,value):
        left_index = 0
        mid_index = 0
        right_index = len(self.data) - 1

        #Loop through the code until the left bound is equal to
        #the right bound, meaning we have traversed the entire 
        #Data Set
        while left_index <= right_index:

            mid_index = (left_index + right_index) // 2
            mid_point = self.data[mid_index]

            #At this point there is only one element between our left and roght bounds
            #thus the midpoint is definately our search value
            if mid_point == value:
                self.value = value
                self.index = mid_index
                return self.index

            if mid_point < value:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        return -1

    def find_all_occurances(self,number):
        index = self.perform_search(number)
        indices = [index]

        i = index-1
        while i >= 0:
            if self.data[i] == number:
                indices.append(i)
            else:
                break
            i = i - 1 

        i = index+1
        while i<len(self.data):
            if self.data[i] == number:
                indices.append(i)
            else:
                break
            i = i + 1

        return sorted(indices)


    def print_result(self):
        print(f"The number {self.value} occurs at indexs : {self.index} ")

#Function initializes the occurance class object
#Declares a sample data set and passes the data set
#to the constructor 
def get_occurance():
    
    #Sample data set
    #numbers = [1,4,6,9,11,13,14,15,17,21,34,34,56] 
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]

    #Initialize an Occurance object passing the sample data set
    #to the constructor
    test = Occurance(numbers)
    
    return test


if __name__ == '__main__':
    number_to_find = 15
    main = get_occurance()
    output = main.find_all_occurances(number_to_find)
    print(f"Indices of {number_to_find} are {output}")

    
