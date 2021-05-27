import itertools
import numpy as np

f = list(map(int, open("inputs/day9.txt", "r").read().split("\n")))
n = len(f)

for i in range(25, len(f)):
    if f[i] not in [sum(j) for j in list(itertools.combinations(f[i - 25 : i], 2))]:
        invalid = f[i]
        print(invalid)
        break

sums = np.zeros((n, n))
for i in range(0, n):
    for j in range(i, n):
        if j == i:
            sums[i][j] = f[j]
        else:
            sums[i][j] = sums[i][j - 1] + f[j]

# print(np.argwhere(sums == invalid)[0]) outputs: 390, 406
print(max(f[390:407]) + min(f[390:407]))
