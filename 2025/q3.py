# EverybodyCodes - Quest 3

import os
import time
from itertools import combinations


# IN_FILE1 = os.path.join("2025","inputs","2025-03-1.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-03-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-03-2.sample.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-03-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-03-3.sample.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-03-3.txt")

data = "5,54,60,35,47,14,47,9,60,43,38,60,74,38,47,40,50,44,11,47,72,81,52,21,12,4,22,23,61,18,1,62,32,48,50,28,15,55,84,12,55,53,5,52,17,29,6,63,14,53,40,48,86,28,12,21,9,4,33,44,30,10,80,45,48,43,56,71,88,21,30,26,3,79,55,19,54,67,86,51,6,50,47,65,6,30,86,53,73,13,21,59,80,77,42,69,14,7,79,21"
# data = "10,5,1,10,3,8,5,2,2"

def parse(IN_FILE):
    """
    Parse
    """

    # with open(IN_FILE) as fp:
    #     data = fp.read().splitlines()


    return [int(x) for x in data.split(",")]




def part1(x):           # => 2532

    x.sort()
    x.reverse()
    x_set = set(x)

    return sum(x_set) 


def part2():           # => 
    data = "91,128,114,85,77,40,28,178,11,54,63,76,64,170,84,133,124,133,130,37,3,97,7,34,170,185,119,113,17,54,61,51,104,184,125,177,188,27,24,125,6,36,170,140,116,162,2,60,40,159,170,94,68,101,172,186,172,46,126,127,125,16,65,93,180,34,159,145,62,46,102,57,89,73,43,21,44,29,92,142,94,13,100,34,17,131,105,111,33,19,76,28,138,104,28,8,71,169,37,137,52,127,184,126,110,156,177,3,78,150,155,89,144,49,24,4,19,169,129,108,188,155,25,91,116,58,105,11,48,127,58,28,78,156,171,10,162,112,133,131,163,30,187,22,3,55,131,5,142,150,75,98,11,88,12,102,46,111,50,118,150,66,56,153,82,181,183,164,5,65,12,137,126,104,19,3,33,183,73,129,126,132,141,113,184,49,35,58,66,129,15,73,143,126,86,104,94,181,186,42,27,75,154,150,161,152,94,38,14,96,150,138,127,167,122,143,12,20,153,57,45,188,25,14,44,52,102,14,26,38,82,170,8,5,153,156,103,86,62,85,92,152,181,76,62,130,134,118,178,162,62,58,146,81,24,179,43,136,184,7,84,67,42,157,50,135,60,47,144,183,33,78,147,147,95,157,16,150,141,76,159,127,144,111,105,159,132,137,16,44,35,170,184,51,87,162,16,55,26,1"
    x = [int(x) for x in data.split(",")]

    x_set = set(x)
    
    x_lst = list(x_set)
    x_lst.sort()
    x_lst.reverse()

    c20 = list(combinations(x_lst, 20))
    min20 = 99999999
    for m in c20:
        s = sum(m)
        if s<min20:
            min20 = s


    return min20


def part3(x):           # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2())
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


