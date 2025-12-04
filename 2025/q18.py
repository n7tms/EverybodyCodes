# EverybodyCodes - Quest 18

import os
import time

DAY = 18

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


    return data


def part1(data):     # => 2056950
    # I did this by hand...drawing out the map and doing the calculations by hand
    return 0



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


