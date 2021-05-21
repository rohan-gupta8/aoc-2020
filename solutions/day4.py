f = open("inputs/day4.txt", "r")
inp = list(f.read().split("\n"))

parsed = []
curr = 0
c = 0
for i in range(len(inp)):
    if inp[i] == "":
        parsed.append("".join([k + " " for k in inp[curr:i]]).strip().split())
        curr = i + 1

parsed.append("".join(inp[(len(inp) - 1)]).strip().split())
valid = []
for i in parsed:
    if len(i) == 8 or (len(i) == 7 and all(["cid" not in j[0:3] for j in i])):
        c += 1
        valid.append(i)

print(f"Part 1: {c}")

c = 0
for i in range(len(valid)):
    for j in range(len(valid[i])):
        valid[i][j] = tuple(valid[i][j].split(":"))

for i in range(len(valid)):
    valid[i] = dict(valid[i])

z29 = list(map(str, list(range(0, 10))))
a2f = ["a", "b", "c", "d", "e", "f"]
for i in valid:

    b1 = 1920 <= int(i["byr"]) <= 2002
    b2 = 2010 <= int(i["iyr"]) <= 2020
    b3 = 2020 <= int(i["eyr"]) <= 2030

    h = i["hgt"]
    b4 = False
    if h[-2:] == "cm":
        b4 = all(char.isdigit() for char in h[:3]) and 150 <= int(h[0:3]) <= 193
    elif h[-2:] == "in":
        b4 = 59 <= int(h[0:2]) <= 76
    b5 = (
        i["hcl"][0] == "#"
        and all([k in a2f or k in z29 for k in i["hcl"][1:]])
        and len(i["hcl"]) == 7
    )
    b6 = i["ecl"] in ["amb", "blu", "brn", "grn", "gry", "hzl", "oth"] and len(i["ecl"]) == 3
    b7 = len(i["pid"]) == 9 and all(char.isdigit() for char in i["pid"])
    if b1 and b2 and b3 and b4 and b5 and b6 and b7:
        c += 1

print(f"Part 2: {c}")
