from itertools import groupby

f = sorted(list(map(int, open("inputs/day10.txt", "r").read().split("\n"))))
f = [0] + f + [max(f) + 3]
diffs = [f[i] - f[i - 1] for i in range(1, len(f))]

# Part 1
print((diffs.count(1)) * (diffs.count(3)))

# Part 2
'''
We use the (weird) observation that you can have at most 5 consecutive numbers in a row.
This is not specified in the writeup, but seems to be important in solving the problem
The math gets pretty intense otherwise (maybe no closed form). 
'''
ans = 1
perms_map = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}  # counted by hand lol
for value, group in groupby(diffs):
    if value == 1:
        ans *= perms_map[len(list(group))]
print(ans)

'''
Wasn't too happy with hacky solution above, so I found a nicer DP-esque solution.
If we think of this list as a topologically sorted DAG, we simply want the number of paths
to the end such that each path doesn't 'hop over' more than 3 integers. Therefore, the
number of paths for item i is simply the sum of the number of paths to each of the 
previous three integers i-1, i-2, and i-3.
'''
m = {0: 1}
for item in f[1:]:
    m[item] = m.get(item - 3, 0) + m.get(item - 2, 0) + m.get(item - 1, 0)

print(m[max(f)])
