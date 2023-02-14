##################################################################################################################
# Selection Sort 
# O(n^2) in Any case scenario since we traverse the data set twice with a nested for loop
##################################################################################################################
def selection_sort(arr):
    
    #Define the length of the data set to limit our loops
    size = len(arr)

    #Outter loop traverses the array checking if the element in the current index is
    #less then the min_index, in which case a swap will be done
    for i in range(size-1):

        #The first element is initially treated as the minimum value
        min_index = i

        #Inner loop traverses the array starting from the second element, checking if the
        #element in the current index is less than the initially defines min value .i.e first 
        #value in array
        #if so then the current value becomes the min value and swaped with min the initial
        #min value thus min_index is updated to current index
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        
        #We only perform a swap if the current element in the outter loop
        #is not equal to the min index
        if i != min_index:
            #We then swap the value in the current index with the value of
            #the min index, this happens until all elements are swapped rightwards
            arr[i],arr[min_index] = arr[min_index],arr[i]
    


if __name__ == "__main__":
    #Define different test cases
    data_set = [   
        [ 3, 9, 8],
        [2, 4],
        [2, 34, 6, 13, 9, 8],
        [9],
        [5, 1, 7],
        [2, 14, 6, 3, 49, 8, 5, 1, 27],
        []
    ]

    for elements in data_set:
        print("#########################################")
        print(elements)
        selection_sort(elements)
        print(elements)