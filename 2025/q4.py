# EverybodyCodes - Quest 4

import os
import time
import math


# IN_FILE1 = os.path.join("2025","inputs","2025-04-1.sample.txt")
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
    # gears = [list(map(int, l.split("|"))) for l in input_str.strip().splitlines() if l.strip()]
    gears = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    num = N
    den = 1
    for a, b in gears:
        num *= b
        den *= a
    return (num + den - 1) // den  # ceiling division

def min_turns3(input_str, N):
    gears = [list(map(int, l.split("|"))) for l in input_str]
    # gears = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    num = N
    den = 1
    for a, b in gears:
        num *= b
        den *= a
    return (num + den - 1) // den  # ceiling division



def part1(gears):           # => 18243

    pairs = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    turn_ratio = 1
    for p1, p2 in pairs:
        turn_ratio = turn_ratio * (p1 / p2)
        
    total_turns = turn_ratio * 2025
    return total_turns




def part2(gears):           # => 2852760736197

    pairs = [list(pair) for pair in zip(gears[:-1], gears[1:])]
    # turn_ratio = 1
    # for p1, p2 in pairs:
    #     turn_ratio = turn_ratio * (p1 / p2)
        
    # first_gear = 10000000000000 / turn_ratio
    # return first_gear

    # print(gears[0], gears[-1])
    # ratio = gears[0] / gears[-1]

    # # first_gear = math.ceil(10000000000000 // ratio)
    # first_gear = 10000000000000 // ratio
    # return first_gear

    return min_turns(gears, 10000000000000)
    



def part3(x):           # => 

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


