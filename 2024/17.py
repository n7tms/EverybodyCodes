# Everybody Codes: 17

import numpy as np
import os
import time 


#################################################################################
# My solution (below) works with the sample, but not my actual data
# This solution uses Prim's Minimum Spanning Tree (MST) algorithm and works:
# https://topaz.github.io/paste/#XQAAAQCpCgAAAAAAAAA0m0pnuFI8c9q4WY2stx6xnaXQh5bemQ8nom3lYY4uJyjFiEW3PbE+/vYE7joaW+VHkBjfBGuBMlTDuFKkkA7i1GxS2WikXilaIerf4D1PEagVHyXg/1hHcurNs0L/Aaxj6dhJ4+x9iOv/ohV21Mchl2K5QRsA3MBoCmhJJZ4bCkjgyChrr6VWuXbKlyKd9WBbffcaaOav7xUnLscLj+4kkOmiV8RLA57S/5FOz/M1b3KGCwh2WKwL5BSUKy2B51rDmXazwEYVq67I4Pyh7oGieJLl6coxnPoaTdZDW+RGweQGf9jezgSVCazSbUjse2cF/jsA+/Pf4hJlMLNF273SArmk5qgKFmOI3mLVkfpdz62Myh7rEKhKep+VBfCXigJFkM6eNy+6ve7NOmPwpbSX7i7F3V0148tsliFdb1m6riGL7kd0Ud6ur/8meHv27Y2zJiWbyz2+hh64tUPry1PqRs3Z4+gdveuktBgrJ2YkXODiifNrWzxQPKfsQgucUCgIwJUkqL9afPtkxF+SCbv8iueZ25DYMaL4JOnb9uq2XzyALBGbyKJySw9tFEN/qAZpsD7UC9anWLIzu9JgekQb/dOAbk2HU6wAsztp4EIeIOH7Yte6IGwBvP40WcfoUoVFUtYpDi1rlsispJ94w16q8SoBDHTjHBYYWfxaH9zjB8cB9WNHbj5ClmFUJFOxSZELUChxlWqTUTJ/UyGUrSLyGdCHGsSaGD4QE6FcWtjJYBgr03YpCW3JQixsUYZxraoR06eLsq466HjcPAjca0R555f12LthuueZ7c4c/FUZYZOx9fglQhnbiYSxRQj86bfJ3xuVwgiYgbwqzr+7UdF3XEg3M0P78LQoERnErl/0z0N7ufGsVT/IlmLnNf0Gm6UqOBaLeZOtsL61jlXv6k2u+dzvj/M55G60mGGeO2VIcePCmyvlwyhDQtsjlMULEETYXt62kuTj0laTWfVYzS2duPuUHa8d4R3A8fPxELFVZDZsOvlXWCqJlfdgbZXUAzvTBurzcWIlJZt5kqaaU8ymJ57dNtuL5pUyHXuSbin05XT6lGNDY1/+jfHnuzBOfFdOap84YFaAD0qA+vxLG+Cu8beWWytzXR/GTwBhFtxhJCuoo7ROekAaMUH4ZYHYSFCURap/3bRZV41i05C32ySacS/DMGwh2dw8xgsEXGIR4/IxY8LsYoRTxh1aCKx2ZSzk5QVzIZtJA1SYpDRZvqmcO2Sb/xJ0jwA=
# Prim's algorithm: https://www.geeksforgeeks.org/dsa/prims-minimum-spanning-tree-mst-greedy-algo-5/
#################################################################################


# IN_FILE1 = os.path.join("2024","inputs","2024-17-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-17-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-17-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-17-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-17-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-17-3.txt")


def manhattan_distance(star1, star2) -> int:
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    constellation = list()
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if c == "*":
                constellation.append([(row,col),99])
    
    return constellation


def part1(constellation):           # => 
    # find the shortest distance from each star to every other star
    idx = 1
    while idx < len(constellation):
        src = constellation[idx-1]
        for star in constellation[idx:]:
            md = manhattan_distance(src[0],star[0])
            if md < src[1]:
                src[1] = md
        idx += 1

    constellation[idx-1][1] = 0

    total = 0
    for star in constellation:
        total += star[1]
    total += len(constellation)

    return total

def part2(data):            # => 
    pass


def part3(data):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(data))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()