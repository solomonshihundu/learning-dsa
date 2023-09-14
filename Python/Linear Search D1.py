def linear_search(arr,value):
    for i in arr:
        if value == 5:
            print(arr.index(value)," ",value)
            return

my_arr = [1,6,3,5,7,9,5,3]

linear_search(my_arr,5)