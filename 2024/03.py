# Everybody Codes: 03

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-03-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-03-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-03-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-03-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-03-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-03-3.txt")

DIRS = [[-1,0],[0,1],[1,0],[0,-1]]
DIRS3 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    earth = np.zeros((len(data),len(data[0])), dtype=int)
    for r in range(0,len(data)):
        for c in range(0,len(data[0])):
            if data[r][c] == "#":
                earth[r][c] = 1
    # print(earth)
    return earth


def is_surrounded(row, col, e, d):
    # iterate through all of the directions (d)
    # if all the cells are the same value as the given cell (row, col) ...
    # ... then the given cell is surrounded.
    flag = True
    for x,y in d:
        if e[row+x][col+y] != e[row][col]:
            flag = False
    return flag


def part1(earth):           # => 124
    blocks = 0

    # Count first layer
    blocks = np.sum(earth)

    # until no blocks are changed, dig deeper
    changed = True
    while changed:
        changed = False
        to_be_changed = []
        for r in range(1,len(earth)-1):           # start at 1,1 (ignoring edges)
            for c in range(1,len(earth[1])-1):
                if is_surrounded(r, c, earth, DIRS) and earth[r][c] > 0:
                    # keep track of which blocks need to be changed
                    to_be_changed.append([r,c])

        if len(to_be_changed) > 0:
            # if there are any blocks to be changed, change them!
            blocks += len(to_be_changed)
            changed = True
            for r1, c1 in to_be_changed:
                earth[r1][c1] += 1

    return blocks


def part2():            # => 2737 (uses part1 code to solve)
    pass


def part3(earth):       # => 10365
    blocks = 0

    # Count first layer
    blocks = np.sum(earth)

    # until no blocks are changed, dig deeper
    changed = True
    while changed:
        changed = False
        to_be_changed = []
        for r in range(1,len(earth)-1):           # start at 1,1 (ignoring edges)
            for c in range(1,len(earth[1])-1):
                if is_surrounded(r, c, earth, DIRS3) and earth[r][c] > 0:
                    to_be_changed.append([r,c])
        if len(to_be_changed) > 0:
            blocks += len(to_be_changed)
            changed = True
            for r1, c1 in to_be_changed:
                earth[r1][c1] += 1

    return blocks


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")


    data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()