def fibonacci(n):
    computed = False
    cache = {}
    fib = fibonacci(n)
    
    for k in cache.keys():
        if k == n:
            computed = True

    if computed:
        #IF input is 0 or 1 return the input itself 
        if n in [0, 1]:
            cache.update({n:n})
            return n
        return cache(n - 1) + cache(n - 2)
    else:
        cache.update({n:fib})
        return fibonacci(n - 1) + fibonacci(n - 2)
        

print(fibonacci(5))
