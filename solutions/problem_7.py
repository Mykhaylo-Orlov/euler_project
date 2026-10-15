from sympy import *
import time
import numpy as np

s = time.time()
index = 1
number = 2
while index != 10001:
    number+=1
    if isprime(number) == True:
        index+=1

print(number)
print ('Brutal force approach time: ', time.time() - s)

# Could use Seive of Eratosthenes (careful with the upper limit)
# Algorithm:
# 1) Set maximum number T
# 2) Do an array from 2 till T
# 3) Assign p variable starting from the first number (2 in our case)
# 4) Eluminate all composites of p, starting from p^2 until the end of an array_numbers
# 5) When done, assign p as the next number (which was not eluminated)
# 6) Repeat until you reach T

# Seive of Eratisthenes implementation


T = 10**6 # 1

is_prime = np.ones(T + 1, dtype=bool) # 2
is_prime[0] = is_prime[1] = False # for 0 and 1

s = time.time()
for p in range(2, int(T**0.5) + 1): # 3/5/6
    if is_prime[p]: 
        is_prime[p**2:T+1:p] = False # 4

primes = np.nonzero(is_prime)[0] # extract only is_prime==True numbers
print(primes[10000])  # The 10,000th prime number
print('Seive Eratosthenes time: ', time.time() - s)






