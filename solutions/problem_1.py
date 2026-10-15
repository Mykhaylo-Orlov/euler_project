import numpy as np
from tqdm import tqdm

s = 0

for i in tqdm(range(1, 1000)):
    if (i % 3)==0 or (i % 5)==0:
        s+=i

print(s)