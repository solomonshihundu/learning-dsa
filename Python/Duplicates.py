import matplotlib.pyplot as plt
import time
import timeit

def duplicates(list):
    st_time = time.time()
    for i in range (len(list)):
        for j in range (i+1,len(list)):
            if list[i] == list[j]:
                print("Duplicate found : ",list[i])
                break
    sp_time = time.time()
    
    tt = sp_time -st_time

    print("Start Time : ",st_time)
    print("Stop Time : ",sp_time)
    print("Time Taken : ",tt)

nums_0 = [1,2,3,4,53,6,71,18,91,2,13,4,5,61,748,9,12,12,31,4,5,6,7,183,9,12,3,24,5,6,17,81,989,2,3,4,5,6,7,188,19,2,3,4,581,36,17,8,9,257,3,4,5,6,7,8,9]
nums_1 = [1,2,3,4,1,2,5,0,9]
nums_2 = [1,20,3,40,5,60,7,8,9]

duplicates(nums_0)
duplicates(nums_1)
duplicates(nums_2)