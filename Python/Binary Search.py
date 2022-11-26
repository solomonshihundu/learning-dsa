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


#Recussive Method
def binary_search_rec(array,value,low,high):

    while low <= high:
        
        mid = low + (high - low)//2

        if value == array[mid]:
            return mid
        elif value < array[mid]:
            binary_search_rec(array,value,low,mid -1)
        else:
            binary_search_rec(array,value,mid + 1,high)

    return -1

b = [1, 2, 3, 5, 7, 9, 12, 12, 22, 27, 56, 67, 87, 134, 324, 333, 405, 546, 876, 9765] 
y = 12
result_rec = binary_search_rec(b,y,0,len(b) -1)
if result_rec != -1:
    print("Value of {num} is at index {index}".format(num = y, index = result_rec))
else:
    print("Not found")
