# EverybodyCodes - Quest 8

import os
import time


IN_FILE2 = os.path.join("2025","inputs","2025-08.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-08-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-08-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-08-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().split(",")


    return data



def part1(data):           # => 61
    nails = [int(x) for x in data]
    nails_cnt = max(nails)
    center = nails_cnt / 2

    pairs = [[a,b] for a, b in zip(nails, nails[1:])]

    thru_center = 0
    for a,b in pairs:
        if abs(a-b) == center:
            thru_center += 1

    return thru_center


def part2(data):     # => 
    nails = [int(x) for x in data]
    nails_cnt = max(nails)
    center = nails_cnt / 2

    pairs = [[a,b] for a, b in zip(nails, nails[1:])]

    knots = 0
    for idx, z in enumerate(pairs):
        a, b = z
        if idx>1:
            for c, d in pairs[:idx]:
                if ():
                    knots += 1

    return knots
    

def part3(x):           # => 

    
    return 0


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

    # n, r = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(n, r))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


