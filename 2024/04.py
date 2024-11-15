# Everybody Codes: 04

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-04-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-04-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-04-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-04-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-04-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-04-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    nails = [int(n) for n in data]
    return nails
    

def part1(nails):           # => 87
    shortest = min(nails)

    hammer_hits = 0
    for n in nails:
        hammer_hits += n - shortest

    return hammer_hits

def part2(nails):            # => 844594
    shortest = min(nails)

    hammer_hits = 0
    for n in nails:
        hammer_hits += n - shortest

    return hammer_hits


def part3(nails):       # => 127387940
    # sort the list and find the middle.
    nails.sort()
    optimum = nails[len(nails)//2]

    # count the hammer hits for each nail
    hammer_hits = 0
    for n in nails:
        hammer_hits += abs(n - optimum)
    
    return hammer_hits


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()