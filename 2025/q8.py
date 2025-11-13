# EverybodyCodes - Quest 8

import os
import time
from itertools import combinations


# IN_FILE3 = os.path.join("2025","inputs","2025-08.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-08-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-08-2.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-08-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().split(",")


    return data



def part1(data):     # => 61
    nails = [int(x) for x in data]
    nails_cnt = max(nails)
    center = nails_cnt / 2

    pairs = [[a,b] for a, b in zip(nails, nails[1:])]

    thru_center = 0
    for a,b in pairs:
        if abs(a-b) == center:
            thru_center += 1

    return thru_center


def part2(data):     # => 2924895
    nails = [int(x) for x in data]
    nails_cnt = max(nails)

    raw_pairs = [[a,b] for a, b in zip(nails, nails[1:])]
    pairs = [sorted(p) for p in raw_pairs]

    knots = 0
    for idx, z in enumerate(pairs):
        a, b = z
        if idx>1:
            for c, d in pairs[:idx]:
                if (a<c<b<d) or (c<a<d<b):
                    knots += 1

    return knots
    

def part3(data):     # => 2791
    nails = [int(x) for x in data]

    # generate the connecting ropes and sort them so the first element is the lower number
    raw_pairs = [[a,b] for a, b in zip(nails, nails[1:])]
    pairs = [sorted(p) for p in raw_pairs]

    # generate all possible cuts
    max_nail = max(nails)
    possible_cuts = [[i,j] for i,j in combinations(range(1,max_nail+1), 2) if min((j-i)%max_nail, (i-j)%(max_nail)) > 1]
    
    # iterate through all the possible cuts, and check for how many existing ropes would be cut.
    max_cuts = 0
    for z in possible_cuts:
        a, b = z
        cuts = 0
        for c, d in pairs:
            if (a<c<b<d) or (c<a<d<b):
                cuts += 1
        # if we are cutting ON a rope (not just across it), then we also have to count the endpoints.
        if [a,b] in pairs:
            cuts += 2

        if cuts > max_cuts:
            max_cuts = cuts

    return max_cuts


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


