import numpy as np
from tqdm import tqdm


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
a = 1
b = 2
c = 0

array_even = np.array([b])

while c <= 4*(10**6):
    c = a + b
    if isEven(c) == True:
        array_even = np.append(array_even, c)
    a = b
    b = c

print(array_even.sum())