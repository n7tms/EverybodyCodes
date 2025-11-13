# EverybodyCodes - Quest 4

import os
import time


# IN_FILE3 = os.path.join("2025","inputs","2025-04-1.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-04-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-04-2.sample.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-04-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-04-3.sample.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-04-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    i_data = [int(d) for d in data]

    return i_data


def parse3(IN_FILE):
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    return data


def min_turns(gears, N):
    gears = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    num = N
    den = 1
    for a, b in gears:
        num *= b
        den *= a
    return (num + den - 1) // den  # ceiling division


def min_turns3(input_str, N):
    gears = [list(map(int, l.split("|"))) for l in input_str]
    first = gears[0][0]
    last = gears[-1][0]

    # recreate the gear list, shifting the first of the next to be the last of the previous
    # 5, 5|10, 10|20, 5 -->> [5,5], [10,10], [10,5]
    new_gears = list()
    for g0, g1 in gears[1:-1]:
        new_gears.append([first, g0])
        first = g1
    new_gears.append([first, last])

    # the total ratio is the found by multiplying the ratio of each of the individual ratios
    # 5/5 * 10/10 * 10/5 = total_ratio    
    total_ratio = 1
    for a, b in new_gears:
        total_ratio *= (a/b)

    return int(total_ratio*N)


def part1(gears):           # => 18243
    pairs = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    turn_ratio = 1
    for p1, p2 in pairs:
        turn_ratio = turn_ratio * (p1 / p2)
        
    total_turns = turn_ratio * 2025
    return total_turns


def part2(gears):           # => 2852760736197
    pairs = [list(pair) for pair in zip(gears[:-1], gears[1:])]

    return min_turns(gears, 10000000000000)
    

def part3(x):           # => 128784641190
    return min_turns3(x, 100)


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

    data = parse3(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


