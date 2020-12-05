import time

start = time.time()

f = open('advent1a.txt', 'r')

nums = sorted([int(i) for i in f.readlines()])

from itertools import combinations

ns = list(combinations(nums, 3))

for i in ns:
    if sum(i) == 2020:
        p = 1
        for j in i:
            p *= j
    break

print(time.time() - start)
input('')