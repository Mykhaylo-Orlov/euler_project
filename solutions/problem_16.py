import time

s = time.time()
var = 2**1000

def sum_dig (number):
    s = 0
    number = str(number)
    for d in number:
        s+=int(d)
    return s

print(sum_dig(var))
print(time.time() - s)

# no analythical solution