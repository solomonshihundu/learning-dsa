# importing the required module
import matplotlib.pyplot as plt
import time
	

def fibonacci(n):
    #IF input is 0 or 1 return the input itself 
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

    
#Get Time Taken for code to run
def monitor(n):
    start_time = time.time()  
    fb = fibonacci(n)
    end_time = time.time() 

    #print("FIbonacci for {num} is {fib}".format(num = n,fib =fb))
    #print("Time Taken : {tt}".format(tt = (end_time - start_time)))


def plot_fibonacci(n):
    print("Started")

    #Store X time axis values
    time = []
    #Store Y number axis values
    number = []

    #Populate both lists
    for x in range(0,n):
        number.append(x)
        time.append(fibonacci(x))

    for i in number:
        # plotting the points
        plt.plot(time, number)
            
        # naming the x axis
        plt.xlabel('x - Time Taken')
        # naming the y axis
        plt.ylabel('y - Number')
            
        # giving a title to my graph
        plt.title('Fibonacci Time Complexity')
            
        # function to show the plot
        plt.show()

        return 0


#fibonacci(70) # 190392490709135
#fibonacci(60) # 1548008755920
#fibonacci(50) # 12586269025
plot_fibonacci(20)