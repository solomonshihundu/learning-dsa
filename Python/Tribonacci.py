def tribonacci(signature, n):
    #Counter
    count = 0
    
    if n <= 0:
        return []

    #if term is less than 3 but greater than 0, return a subset of list equal to number of terms
    if n < 3:
        return signature[:n]
    else:
        while count < n - 3:
            #Value to store our final summation
            sum = 0
            #Create a subset of the list containing the last three digits
            m = signature[-3:]
            #Loop through list subset summing values
            for i in m:
                sum += i
            signature.append(sum)
            count += 1

        return signature
   
nums = [3, 2, 1]
#nums = [1, 1, 1] # 1 
#nums = [300, 200, 100] # 0
#nums = [1, 1, 1]  #[10]  #[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
#nums = [0, 0, 1] #[10]  #[0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
#nums = [0, 1, 1] #[10] #[0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
print(tribonacci(nums,10))

###################################################################################
#BEST PRACTISE ONE
###################################################################################

def tribonacci_best(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

print(tribonacci_best(nums,10))
###################################################################################
#BEST PRACTISE TWO
###################################################################################

def tribonacci_best_2(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]


print(tribonacci_best_2(nums,10))