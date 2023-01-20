def fibonacci(n):
    #Cache to store evaluated values
    cache = {}

    #Value already evaluated
    num = 0
    fib_num = 0

    #If input is 0 or 1 return the input itself 
    if n in [0, 1]:
        cache.update({n:n})
        return n

    for j,k in cache.items():
        #Fibonacci already evaluated
        #retrive fibonacci
        if n == j:
            fibonacci(n)
        
        #fibonacci not yet evaluated
        #Evaluate fibonacci
        #Store number and fib in cache
        else:
            fib_num = 


    
    #fb = fibonacci(n - 1) + fibonacci(n - 2)
    #cache.update({n:fibonacci(fb)})
    #print(cache)
    #return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(9)


def fibonacci(n):
    #IF input is 0 or 1 return the input itself 
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
