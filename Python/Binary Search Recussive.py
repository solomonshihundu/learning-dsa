#################################################################################################################################
# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)
# space complexity of the binary search is O(1)
#################################################################################################################################
#Recussive Method
def binary_search_rec(array,value,low,high):

    if high >=   low:
        
        mid = low + (high - low)//2

        #Value is at midpoint, return index
        if value == array[mid]:
            return mid
        #Search left
        elif value < array[mid]:
            return binary_search_rec(array,value,low,mid -1)
        #Search right
        else:
            return binary_search_rec(array,value,mid + 1,high)

    return -1

b = [1, 2, 3, 5, 7, 9, 12, 12, 22, 27, 56, 67, 87, 134, 324, 333, 405, 546, 876, 9765] 
y = 12
result_rec = binary_search_rec(b,y,0,len(b) -1)
if result_rec != -1:
    print("Value of {num} is at index {index}".format(num = y, index = result_rec))
else:
    print("Not found")