# EverybodyCodes - Quest 4

import os
import time
import math


# IN_FILE1 = os.path.join("2025","inputs","2025-04-1.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs","2025-04-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-05-2.sample.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-05-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-05-3.sample.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-05-3.txt")

# data = "58:5,3,7,8,9,10,4,5,7,8,8"
data1 = "58:7,1,8,6,3,8,8,1,5,8,9,2,4,6,2,3,9,8,5,9,3,6,8,3,1,7,9,3,1,9"


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    # i_data = [int(d) for d in data]

    return data



def build_sword(values):
    quality = ""

    x = values.split(":")
    id = x[0]
    numbers = [int(n) for n in x[1].split(",")]

    sword = [[None, numbers[0], None]]
    quality += str(numbers[0])
    for n in numbers[1:]:
        used = False
        for segment in sword:
            l,h,r = segment
            if not l and n < h:
                segment[0] = n
                used = True
                break
            elif not r and n > h:
                segment[2] = n
                used = True
                break
        
        if not used:
            sword.append([None, n, None])
            quality += str(n)

    return int(quality)


def build_sword3(values):
    quality = ""

    x = values.split(":")
    id = x[0]
    numbers = [int(n) for n in x[1].split(",")]

    sword = [[None, numbers[0], None]]
    quality += str(numbers[0])
    for n in numbers[1:]:
        used = False
        for segment in sword:
            l,h,r = segment
            if not l and n < h:
                segment[0] = n
                used = True
                break
            elif not r and n > h:
                segment[2] = n
                used = True
                break
        
        if not used:
            sword.append([None, n, None])
            quality += str(n)

    new_sword = []
    for s in sword:
        segment = ""
        for sn in s:
            if sn:
                segment += str(sn)
        new_sword.append(int(segment))

    return [int(id), int(quality), new_sword]



def part1():           # => 7685438387
    return build_sword(data1)


def part2(swords):     # => 8994512994861
    qualities = []

    for sword in swords:
        qualities.append(build_sword(sword))

    diff = max(qualities) - min(qualities)

    return diff
    

def part3(x):           # => 31769825
    qualities = []

    for line in x:
        qualities.append(build_sword3(line))

    sorted_swords = sorted(qualities, key=lambda x: (x[1], x[2], x[0]), reverse=True)

    checksum = 0
    for idx, sword in enumerate(sorted_swords):
        checksum += ((idx+1) * sword[0])

    return checksum


def solve():
    """Solve the puzzle for the given input."""
    # data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1())
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


