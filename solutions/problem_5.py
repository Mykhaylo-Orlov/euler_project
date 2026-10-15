from tqdm import tqdm

list_values = []

for i in range(1, 21):
    list_values.append(i)

value = 21
while True:
    counter = 0
    for i in list_values:
        if value % i != 0:
            value+=1
            break
        elif value % i == 0:
            counter +=1
    if counter == 20:
        break

    

print(value)

# Or by Fundamental theorem of arithmetics 2^4*3^2*5*7*11*13*17*19
