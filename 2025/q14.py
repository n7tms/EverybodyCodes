# EverybodyCodes - Quest 14

import os
import time

DAY = 14

IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
# IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    floor = []
    for r, line in enumerate(data):
        row = []
        for c, tile in enumerate(line):
            if tile == ".":
                row.append(False)
            else:
                row.append(True)
        floor.append(row)
    
    return floor


def odd_neighbors(f: list, loc: list) -> bool:
    # return true if this tile needs to change

    DIRs = [[-1,-1],[-1,1],[1,-1],[1,1]]

    a,b = loc
    neighbors = 0
    for c,d in DIRs:
        if a+c >= 0 and b+d >= 0 and a+c < len(f) and b+d < len(f[0]):
            if f[a+c][b+d]: neighbors += 1
    
    if (neighbors in [0,2,4]) and not f[a][b]:
        return True
    elif (neighbors in [0,2,4]) and f[a][b] == True:
        return True

    return False


def sum_tiles(f: list) -> int:
    at = 0
    for row in f:
        at += sum(row)
    
    return at


def part1(data: list):     # => 
    rounds = 10
    active_tiles = 0
    for rnd in range(rounds):
        tmp_data = data.copy()
        for r,row in enumerate(data):
            for c,tile in enumerate(row):
                if odd_neighbors(data, [r,c]):
                    tmp_data[r][c] = not tmp_data[r][c]

        active_tiles += sum_tiles(tmp_data)
        data = tmp_data[:]
  
    return active_tiles



def part2(data):     # => 

    return 0



def part3(data):     # => 

    return 0


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(x))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


