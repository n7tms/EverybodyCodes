# Everybody Codes: 05

import numpy as np
import os
import time


IN_FILE1 = os.path.join("2024","inputs","2024-05-1.sample.txt")
# IN_FILE1 = os.path.join("2024","inputs","2024-05-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-05-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-05-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-05-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-05-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    x = [line.split() for line in data]

    # convert all elements to ints
    y = [[int(item) for item in rw] for rw in x]

    # rotate the matrix CCW
    t = list(reversed(list(zip(*y))))

    # return the matrix back to the program
    return t
    

def part1(clappers):           # => 
    # start with last row
    # pop digit from front of row
    # clap
    #   if clapper =< row count, insert clapper into position (clapper - 1)
    #   if clapper > row count, insert clapper into position (clapper - row count)
    # print first digit in each row, from last to first.

    for r,items in enumerate(clappers[::-1]):
        print(str(r) + ": " + str(items))


def part2():            # => 
    pass

def part3():       # => 
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