import time
import threading

def calc_square(nums):
    print("Cslculating Squares")
    for n in nums:
        time.sleep(0.2)
        print('Square {sq} : '.format(sq = n),n*n)

def calc_cube(nums):
    print("Calculating Cubes")
    for n in nums:
        time.sleep(0.2)
        print('Cube {cube} : '.format(cube = n),n*n*n)

arr = [1,2,3,4,5,6,7,8]

t = time.time()

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

# Without Threading TT = 3.2389092445373535
# With MultiThreading TT = 1.6078991889953613
print("Done in : ",time.time() - t) 