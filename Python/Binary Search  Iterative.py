#################################################################################################################################
# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)
# space complexity of the binary search is O(1)
#################################################################################################################################
#Iterative Method
def binary_search(array,value,lower_b,upper_b):
    
    #While keeping within the array size limit
    while lower_b <= upper_b:
        
        midpoint = lower_b + (upper_b - lower_b)//2

        if value == array[midpoint]:
            return midpoint
           # return "Value {num} is at {index}".format(num = array[midpoint], index = midpoint)
        elif value < array[midpoint]:
            upper_b = midpoint - 1
        else:
            lower_b = midpoint + 1
            
    return -1

a = [1, 2, 3, 5, 7, 9, 12, 12, 22, 27, 56, 67, 87, 134, 324, 333, 405, 546, 876, 9765] 
x = 546
result = binary_search(a,x,0,len(a) -1)
if result != -1:
    print("Value of {num} is at index {index}".format(num = x, index = result))
else:
    print("Not found")


