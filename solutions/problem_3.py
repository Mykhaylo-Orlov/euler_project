import numpy as np

number = 600851475143
list_factors = []


for i in range(2, number):

    if number%i == 0:
        
        list_factors.append(i)

        number = number/i
    if number == 1:
        break


print(max(list_factors))