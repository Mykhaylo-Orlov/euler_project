import time



s = time.time()
for c in range(2, 1000): # since a+b+c=1000, we know for sure that c can not be greater than 1000
    for b in range(2, c): # since we know that b<c always
        a = 1000 - b - c # since we know that a+b+c=1000
        if a > 0 and a**2 + b**2 == c**2: # if Pif. condition is fulfilled and a+b+c=1000 is fulfilled
            print(a * b * c) # result
            print(f"Triplet: a={a}, b={b}, c={c}")
            break
    else:
        continue
    break

print(f"Time taken: {time.time() - s:.6f} seconds")


# Analythical solution using rule : a=2mn, b=m^2-n^2, c=m^2+n^2, where m>n>0 and are whole numbers.
# In general, this way can generate Pif. triplets.
