import numpy as np
from copy import deepcopy

grid = np.array([list(i) for i in open("inputs/day11.txt", "r").read().split("\n")])
x = grid.shape[0]
y = grid.shape[1]

# Part 1: most inefficient solution world

while True:
    flag = True
    padded = np.pad(grid, 1, mode="constant", constant_values="L")
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if (
                not np.any(padded[i - 1 : i + 2, j - 1 : j + 2] == "#")
                and padded[i][j] == "L"
            ):
                grid[i - 1][j - 1] = "#"
                flag = False
            elif (
                np.count_nonzero(padded[i - 1 : i + 2, j - 1 : j + 2] == "#") >= 5
                and padded[i][j] == "#"
            ):
                grid[i - 1][j - 1] = "L"
                flag = False
    if flag:
        print(np.count_nonzero(grid == "#"))
        break

# Part 2: also most inefficient solution world
grid = np.array([list(i) for i in open("inputs/day11.txt", "r").read().split("\n")])


def num_visible_occupied(arr, x, y):
    count = 0
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for (dx, dy) in deltas:
        nx, ny = (x + dx, y + dy)
        while (0 <= nx <= len(arr) - 1) and (0 <= ny <= len(arr[0]) - 1):
            if arr[nx][ny] == "L":
                break
            if arr[nx][ny] == "#":
                count += 1
                break
            nx, ny = (nx + dx, ny + dy)
    return count


while True:
    flag = True
    copy = deepcopy(grid)
    for i in range(0, x):
        for j in range(0, y):
            if num_visible_occupied(copy, i, j) == 0 and copy[i][j] == "L":
                grid[i][j] = "#"
                flag = False
            elif num_visible_occupied(copy, i, j) >= 5 and copy[i][j] == "#":
                grid[i][j] = "L"
                flag = False
    if flag:
        print(np.count_nonzero(grid == "#"))
        break
