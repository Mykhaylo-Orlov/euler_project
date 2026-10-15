list_values = []

for i in range(998, 99, -1):
    for j in range(998, 99, -1):
        if (i%11==0) or (j%11==0): # idea from analythical solution
            if str(i*j) == str(i*j)[::-1]:
                list_values.append(i*j)
        
print(max(list_values))



# Analythical solution by using: abccba : 100000*a + 10000*b + 1000*c + 100*c + 10*b + 1 * a = 11(9091a + 910b + 100c)