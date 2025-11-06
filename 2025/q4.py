# EverybodyCodes - Quest 4

import os
import time


# IN_FILE1 = os.path.join("2025","inputs","2025-04-1.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-04-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-04-2.sample.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-04-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-04-3.sample.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-04-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()


    return 




def part1(x):           # => 

    return


def part2(x):           # => 

    return 

    
def part3(x):           # => 

    return 


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


