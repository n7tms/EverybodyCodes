# EverybodyCodes - Quest 13

import os
import time
from collections import deque
from itertools import chain

DAY = 13

IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    # dial = [0] * (len(data) + 1)
    # dial[0] = 1
    # pos = 0
    # idx = 1
    # for d in data:
    #     if pos == 0: # on the right
    #         dial[idx] = int(d)
    #         pos = 1
    #     else:
    #         dial[-idx] = int(d)
    #         pos = 0
    #         idx += 1

    # return dial


    nums = [int(x) for x in data]
    right_side = nums[::2]        # first, third, fifth... → go right
    left_side = nums[1::2]        # second, fourth... → go left (farthest first)
    return [1] + right_side + left_side[::-1]
    



def parse2(IN_FILE):
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    dial = [0] * (len(data) + 1)
    dial[0] = [1]
    pos = 0
    idx = 1
    for d in data:
        s, e = d.split("-")
        if pos == 0: # on the right
            dial[idx] = [x for x in range(int(s), int(e)+1)]
            pos = 1
        else:
            tmp = [x for x in range(int(s), int(e)+1)]
            tmp.reverse()
            dial[-idx] = tmp
            pos = 0
            idx += 1

    new_dial = [item for sublist in dial for item in sublist]
    return new_dial





def part1(data):     # => 933
    turns = 2025
    num = data[turns % len(data)]

    return num



def part2(data):     # => 1989
    turns = 20252025
    num = data[turns % len(data)]
    return num



def part3(data):     # => 87640
    turns = 202520252025
    num = data[turns % len(data)]
    return num


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x = parse2(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    x = parse2(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(x))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


