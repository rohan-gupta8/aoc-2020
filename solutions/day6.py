f = open("inputs/day6.txt", "r").read().split("\n")

totalc, groupstr = 0, ""

# Part 1
for line in f:
    if line == "":
        totalc += len(set(list(groupstr)))
        groupstr = ""
    else:
        groupstr += line

print(totalc)

# Part 2

totalc = 0
groupstr = ""
groupsize = 0
for line in f:
    if line == "":
        groupset = set(list(groupstr))
        totalc += sum([1 if groupstr.count(i) == groupsize else 0 for i in groupset])
        groupstr = ""
        groupsize = 0
    else:
        groupstr += line
        groupsize += 1


print(totalc)
