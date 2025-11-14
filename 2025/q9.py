# EverybodyCodes - Quest 9

import os
import time
from itertools import combinations


# IN_FILE3 = os.path.join("2025","inputs","2025-09.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-09-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-09-2.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-09-3.txt")



def parse(IN_FILE):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    dna = list()
    for line in data:
        id, seq = line.split(":")
        dna.append([int(id),seq])

    return dna



def part1(data):     # => 6512
    p1 = data[0][1]
    p2 = data[1][1]
    c = data[2][1]

    p1_cnt = 0
    p2_cnt = 0
    for i, sym in enumerate(c):
        if p1[i] == sym:
            p1_cnt += 1
        if p2[i] == sym:
            p2_cnt += 1

    degree = p1_cnt * p2_cnt  
    return degree


def relationship(child, p1, p2) -> int:

    p1_cnt = 0
    p2_cnt = 0
    for i, sym in enumerate(child):
        match = False
        if p1[i] == sym:
            match = True
            p1_cnt += 1
        if p2[i] == sym:
            match = True
            p2_cnt += 1
        
        if not match:
            return 0
    
    return p1_cnt * p2_cnt



def part2(data):     # => 317403
    n = len(data)
    results = list()

    for child_idx in range(n):
        child = data[child_idx][1]
        for i,j in combinations(range(n), 2):
            if i == child_idx or j == child_idx: continue
            results.append(relationship(child, data[i][1], data[j][1]))

    return sum(results)
    

def add_to_family(families, c, p1, p2):
    new_fam = families.copy()
    fam_part = [c,p1,p2]
    for f in new_fam:
        if c in f or p1 in f or p2 in f:
            # new_fam.append(f + [c,p1,p2])
            fam_part = fam_part + f
    families.append(list(set(fam_part)))
    return families



def part3(data):     # => 36834
    n = len(data)
    results = list()
    families = list()

    for child_idx in range(n):
        child = data[child_idx][1]
        for i,j in combinations(range(n), 2):
            if i == child_idx or j == child_idx: continue

            if relationship(child, data[i][1], data[j][1]):
                add_to_family(families, data[child_idx][0], data[i][0], data[j][0])

    max_val = 0
    for f in families:
        if sum(f) > max_val:
            max_val = sum(f)

    return max_val


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    x = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(x))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


