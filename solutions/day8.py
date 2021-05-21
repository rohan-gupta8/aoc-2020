f = [i.split() for i in open("inputs/day8.txt", "r").read().split("\n")]


def main(f):
    seen = [False] * len(f)
    p, acc = 0, 0
    while p < len(f) and not seen[p]:
        c, val = f[p]
        seen[p], p = True, p + 1
        if c == "acc":
            acc += int(val)
        if c == "jmp":
            p += int(val) - 1
    return p >= len(f), acc


print(main(f)[1])

for i, (c, n) in enumerate(f):
    c2 = {"acc": "acc", "jmp": "nop", "nop": "jmp"}[c]
    loops, acc = main(f[:i] + [(c2, n)] + f[i + 1 :])
    if loops:
        print(acc)
        break
