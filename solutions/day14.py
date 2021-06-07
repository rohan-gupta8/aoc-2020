import re

f = open("inputs/day14.txt", "r").read().split("\n")
mem = {}
for line in f:
    pre, post = line.split("=")
    if "mask" in pre:
        mask = post.strip()
    else:
        idx = re.search("(\d+)", pre).group()
        data = list(bin(int(post.strip()))[2:])
        mod = ["0" for _ in range(len(mask) - len(data))] + data
        mem[idx] = int(
            "".join([mod[i] if mask[i] == "X" else mask[i] for i in range(len(mask))]),
            2,
        )

print(sum(mem.values()))


def per(n):
    outputs = []
    for i in range(1 << n):
        s = bin(i)[2:]
        s = "0" * (n - len(s)) + s
        outputs.append(list(s))
    return outputs


# Part 2:


def get_addresses(mask, addy):
    addys = []
    addy = list(bin(addy)[2:])
    addy = ["0" for _ in range(len(mask) - len(addy))] + addy
    result = [
        "X" if mask[i] == "X" else str(int(mask[i]) or int(addy[i]))
        for i in range(len(mask))
    ]
    idxs = [i for i in range(len(result)) if result[i] == "X"]
    n = len(idxs)
    l = per(n)
    for i in l:
        temp = result
        for j in range(n):
            temp[idxs[j]] = i[j]
        addys.append(int("".join(temp), 2))
    return addys


mem = {}
for line in f:
    pre, post = line.split("=")
    if "mask" in pre:
        mask = post.strip()
    else:
        idx = int(re.search("(\d+)", pre).group())
        addys = get_addresses(mask, idx)
        value = int(post.strip())
        for a in addys:
            mem[a] = value

print(sum(mem.values()))
