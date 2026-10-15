import time 
import numpy as np
from scipy.special import factorial


start = time.time()
n = factorial(100, exact=True)
print(n)
s = 0

for dig in str(n):
    s+=int(dig)

print('Sum:', s)
print(time.time() - start)
