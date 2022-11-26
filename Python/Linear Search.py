def linear_search(array,value):
    for x in array:
        if x == value:
            print("Your lucky number is : {num}".format(num = x))
            return
        else:
            print("Sorry ! Number Not found")


a = [2,5,12,324,546,3,12,56,134,67,87,1,405,7,22,876,333,9,9765,27]
b = sorted(a)
num = 700
linear_search(a,num)
print('#'*30)
linear_search(b,num)


