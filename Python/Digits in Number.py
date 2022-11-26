#Best method to use
#Considering time taken

import time

num = 12345

then = time.time()
#Method 1
for i in iter(str(num)):
	print(i)
now = then = time.time()
print("Method 1 time taken :: {tt} milliseconds".format(tt = then))


#Method 2
then = time.time()
for digit in str(num):
	print(digit)
now = then = time.time()
print("Method 2 time taken :: {tt} milliseconds".format(tt = then - now))

#Method 3
then = time.time()
while num > 0:
	num, digit = divmod(num, 10)
	print(digit)
now = then = time.time()
print("Method 3 time taken :: {tt} milliseconds".format(tt = then - now))

#Method 4
then = time.time()
for c in map(int, str(num)):
	print(c)
now = then = time.time()
print("Method 4 time taken :: {tt} milliseconds".format(tt = then - now))