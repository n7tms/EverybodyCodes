# EverybodyCodes - Quest 9

import os
import time
from itertools import combinations


IN_FILE1 = os.path.join("2025","inputs","2025-10.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs","2025-10-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-10-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-10-3.txt")

dragon_moves = list()
r_max = 0
c_max = 0
r_ctr, c_ctr = 0,0

def parse(IN_FILE):
    """
    Parse
    """
    global r_max, c_max, r_ctr, c_ctr
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    sheep = list()
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                sheep.append([r,c])
    
    r_max = len(data)
    c_max = len(data[0])
    # find center of board
    r_ctr = (len(data) // 2) + 1
    c_ctr = (len(data[0]) // 2) + 1

    return sheep


def get_dragon_moves(to_check: list, depth:int, target_depth: int):
    global dragon_moves

    loc = to_check.pop()
    dragon_moves.append(loc)
    if depth >= target_depth: return

    r,c = loc
    if r-2 >= 0 and c-1 >= 0:
        to_check.append([r-2, c-1])
    if r-2 >= 0 and c+1 < c_max:
        to_check.append([r-2, c+1])
    if r-1 >= 0 and c+2 < c_max:
        to_check.append([r-1, c+2])
    if r+1 < r_max and c+2 < c_max:
        to_check.append([r+1, c+2])
    if r+2 < r_max and c+1 < c_max:
        to_check.append([r+2, c+1])
    if r+2 < r_max and c-1 >= 0:
        to_check.append([r+1, c-1])
    if r+1 < r_max and c-2 >= 0:
        to_check.append([r+1, c-2])
    if r-1 >= 0 and c-2 >=0:
        to_check.append([r-1, c-2])

    if to_check:
        get_dragon_moves(to_check, depth+1, target_depth)
    else: 
        return
    



def part1(data):     # => 


    # find all possible dragon moves
    get_dragon_moves([[r_ctr, c_ctr]], 0, 1)

    # compare dragon moves with sheep locations

    # return number of "intersections"

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


