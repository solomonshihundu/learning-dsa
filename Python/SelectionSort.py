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
        #element in the current index is less than the intially defines min value.
        #if so then the minimun index is updated to the current index. 
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
    data_set = [2, 4, 6, 3, 9, 8, 5, 1, 7]
    print(data_set)
    selection_sort(data_set)
    print(data_set)