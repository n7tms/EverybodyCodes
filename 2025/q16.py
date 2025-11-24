# EverybodyCodes - Quest 16

import os
import time

DAY = 16

# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().split(",")

    data = [int(x) for x in data]

    return data


def part1(data):     # => 
    wall = [0] * 91

    for num in data:
        for idx in range(1,len(wall)):
            if idx % num == 0:
                wall[idx] += 1
    
    total = sum(wall)
    return total



def part2(data: list):     # => 
    wall = data[:]

    source = []

    for x in range(1,91):
        if wall[x-1] > 0:
            source.append(x)
            wall[x-1::x] = [w - 1 for w in wall[x-1::x]]

    total = 1
    for s in source:
        total *= s

    return total 



def part3(data):     # => 

    ttl = sum(data)
    
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

    x = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(x))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


