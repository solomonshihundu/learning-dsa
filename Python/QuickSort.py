#################################################################################################################
# Quick sort or Partion Exchange Sort 
# Best Case O(nlongn) : Since we are reducing the search area with every iteration  
# Worst Case O(n^2)   : The array is alrerady sorted thus end up with extreamly unbalance partions
#################################################################################################################
#Generates random integer numbers
from DataGenerator import Generator

#Times method execution time
from Decorators import time_it

#Performs the classic swap
def swap(a,b,arr):
    if a != b:
        arr[a],arr[b] = arr[b],arr[a]

#Applies the divide and conqure rule to split the array
#into two partions separated with the pivot value in the
# its right position, this is done recursively until
#Every subpartion created is sorted thus ending up with
#A sorted array.
def partition(start,end,elements):
    #Initilize the pivot as the first value in the array/partion 
    pivot_index = start
    pivot = elements[pivot_index]

    
    while start < end:
        #Ensuring we are between the array bounds 
        #As long as the element in the start index is less or equal to our pivot
        #We increament the start index traversing right through the array
        #If we get to a value that is greater than the pivot, we stop at this index
        while start < len(elements) and (elements[start] <= pivot):
            start += 1

        #Also as long as the element in the end index is greater than our pivot
        #We decrease the end index traversing left through the array, if we get
        #to a value that is less than the pivot, we stop at this index
        while (elements[end] > pivot):
            end -= 1

        #As long as the start and end index haven't crossed, swap the elements in start and end indecies
        if start < end:
            swap(start,end,elements)

    #In the case that the start and end elements have crossed
    #meaning the end index is greater than the start index
    #swap the pivot and element in the end index.
    #This will set the pivot element in its rightful position
    #Thus elements to the left of the pivot are now less, and those to the right are
    #greater. This process is repeated for all subarrys until the array gets
    #sorted.
    swap(pivot_index,end,elements)

    #We return the end index, which is the now the index of the pivot,this index separates
    #our two partions and will help mark the end of the left partion and start of the right partion
    return end

#Called recursively, by setting the start element i.e pivot to its rightful posiotion
# with every call to the partions and sub partions will eventially end up with a sorted 
# array
@time_it
def quick_sort(start,end,elements):
    #This process occurs as long as the start and end indecies haven't crossed
    #and if so would mean that the entier array has been sorted.
    if start < end:
        pi = partition(start,end,elements)
        quick_sort(start,pi-1,elements)
        quick_sort(pi+1,end,elements)
    

if __name__ == '__main__':
    gen = Generator(1,10)
    elements = gen.generate_data("RAND")
    print(elements)
    quick_sort(0,len(elements) -1,elements)
    print(elements)