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


dragon_moves = []

def get_dragon_moves(start, depth, target_depth):
    global dragon_moves
    r, c = start

    # Add current position
    dragon_moves.append([r, c])

    # Don't go deeper than target_depth
    if depth >= target_depth:
        return

    # Knight moves
    deltas = [
        (-2, -1), (-2, +1),
        (-1, -2), (-1, +2),
        (+1, -2), (+1, +2),
        (+2, -1), (+2, +1),
    ]

    # Explore each valid move
    for dr, dc in deltas:
        nr, nc = r + dr, c + dc
        if 0 <= nr < r_max and 0 <= nc < c_max:
            get_dragon_moves([nr, nc], depth + 1, target_depth)
    



def part1(data):     # => 


    # find all possible dragon moves
    get_dragon_moves([r_ctr, c_ctr], 0, 3)
    print(len(dragon_moves))

    # compare dragon moves with sheep locations
    sxd = list()
    for d in data:
        if d in dragon_moves:
            sxd.append(d)
    
    # return number of "intersections"

    return len(sxd)



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


