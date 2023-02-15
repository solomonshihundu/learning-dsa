####################################################################################################
# Insertion Sort
# Best Case O(n) : n compariosons, 1 swap
# Worst Case O(n^2) : n swaps and n comparisons
# Avg Case O(n^2)
####################################################################################################
def insertion_sort(data):

    #Length on data set to limit our loop
    size = len(data)
    
    #Outter loop staring from the second element, the first element is the sorted list by default
    #Iterates our unsorted list, runs increamentally to the right
    for i in range(1,size-1):
        #Stores the element in comparison
        #Frees the space for insertion to take place
        temp = data[i]
        
        #counter for our sorted list, run decrementally to the left
        #Initialized as one index less relative to the outter loop index
        j = i - 1

        #Ensuring we don't exceed the lower bound
        #Check if the element just before the current index in the list is greater,
        #if so insert that element into the current index  (i), creating a space for
        # insertion of the temp once the conditions become untrue
        #iterate through the sorted array leftwards checking for these condition
        while(j >= 0 and data[j] > temp):
            data[j+1] = data[j]
            j -= 1
        #Ultimately if the list is sorted, then insert the temp value in the space left
        data[j+1] = temp
    


if __name__ == '__main__':
    data_set = [20,72,1,30,6,13,9,5,15,11,2,90,23]
    print(data_set)
    insertion_sort(data_set)
    print(data_set)