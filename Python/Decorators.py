import time
from DataGenerator import Generator

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start)*1000) + " mille seconds")
        return result
    return wrapper

##########################################################################################
# Test Methods for the timer function
##########################################################################################
@time_it
def calc_sqaure(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result

@time_it
def calc_cube(nums):
    result = []
    for num in nums:
        result.append(num*num*num)
    return result

if __name__ == '__main__':
    
    gen = Generator(1,400000)
    data_set = gen.generate_data()

    calc_sqaure(data_set)
    calc_cube(data_set)