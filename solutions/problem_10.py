import time
import numpy as np



T = 2*10**6 # 1

is_prime = np.ones(T + 1, dtype=bool) # 2
is_prime[0] = is_prime[1] = False # for 0 and 1

s = time.time()
for p in range(2, int(T**0.5) + 1): # 3/5/6
    if is_prime[p]: 
        is_prime[p**2:T+1:p] = False # 4

primes = np.nonzero(is_prime)[0] # extract only is_prime==True numbers
print(primes)
print(np.sum(primes))  # The 10,000th prime number
print('Seive Eratosthenes time: ', time.time() - s)
