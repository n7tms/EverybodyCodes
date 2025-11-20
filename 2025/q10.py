# EverybodyCodes - Quest 9

import os
import time
from itertools import combinations


# IN_FILE2 = os.path.join("2025","inputs","2025-10.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-10-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-10-2.txt")
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
    r_ctr = (len(data) // 2)
    c_ctr = (len(data[0]) // 2)

    return sheep


def parse2(IN_FILE):
    global r_max, c_max, r_ctr, c_ctr
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    sheep = list()
    safes = list()
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                sheep.append([r,c])
            elif col == "#":
                safes.append([r,c])
    
    r_max = len(data)
    c_max = len(data[0])
    # find center of board
    r_ctr = (len(data) // 2)
    c_ctr = (len(data[0]) // 2)

    return sheep, safes


dragon_moves = []
last_dragon_moves = []

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



def get_dragon_moves2(ldm: list, move: int):
    global dragon_moves, last_dragon_moves
    
    additional_moves = []

    # Knight moves
    deltas = [
        (-2, -1), (-2, +1),
        (-1, -2), (-1, +2),
        (+1, -2), (+1, +2),
        (+2, -1), (+2, +1),
    ]

    for r,c in ldm:
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0+move <= nr < r_max and 0 <= nc < c_max:
                additional_moves.append([nr, nc])
    
    # remove duplicates
    additional_moves = [list(tup) for tup in {tuple(pos) for pos in additional_moves}]

    last_dragon_moves = additional_moves[:]
    dragon_moves += additional_moves[:]



def part1(data):     # => 145
    # find all possible dragon moves
    get_dragon_moves([r_ctr, c_ctr], 0, 4)
    # print(len(dragon_moves))

    # compare dragon moves with sheep locations
    sxd = list()
    for d in data:
        if d in dragon_moves:
            sxd.append(d)
    
    # return number of "intersections"

    return len(sxd)


def advance_sheep(sh):
    new_sheep = list()
    for r,c in sh:
        r += 1
        if r < r_max:
            new_sheep.append([r,c])
    return new_sheep


def part2(sh: list, sa: list):     # => 1727 is the correct answer
    global dragon_moves, last_dragon_moves

    total_eaten_sheep = 0
    dragon_moves = list()
    last_dragon_moves = [[r_ctr, c_ctr]]

    for move in range(20):
        eaten_sheep = 0
        # get_dragon_moves([r_ctr, c_ctr], 0, move+1)
        get_dragon_moves2(last_dragon_moves, move)
        dragon_moves = sorted([list(tup) for tup in {tuple(pos) for pos in dragon_moves}])

        # if this is the first move, then the center is not a viable move.
        # if move == 0:
        #     dragon_moves.remove([r_ctr, c_ctr])

        # remove safes from dragon moves
        for d in dragon_moves[:]:
            if d in sa:
                dragon_moves.remove(d)

        # Dragon's turn; eat the sheep he moved onto.        
        gone_sheep = list()
        for d in dragon_moves:
            if d in sh:
                if d not in gone_sheep:
                    gone_sheep.append(d)
        eaten_sheep += len(gone_sheep)

        # Remove the eaten sheep
        for x in gone_sheep:
            sh.remove(x)
        
        # Sheep's move
        sh = advance_sheep(sh)

        # Eat the sheep that landed on where the dragon currently is.
        gone_sheep = list()
        for d in dragon_moves[:]:
            if d in sh:
                if d not in gone_sheep:
                    gone_sheep.append(d)
        eaten_sheep += len(gone_sheep)

        # Remove the eaten sheep
        for x in gone_sheep:
            if x in sh: sh.remove(x)

        # Display the status of the round
        print(f"Round: {move}    Eaten Sheep so far: {eaten_sheep}")

        total_eaten_sheep += eaten_sheep

    return total_eaten_sheep
    


def part3(data):     # => 2262549661306 is the correct answer (if you ever get here! this is hard!!)

    return 0


def solve():
    """Solve the puzzle for the given input."""
    # x = parse(IN_FILE1)
    # start_time = time.time()
    # p1 = str(part1(x))
    # exec_time = time.time() - start_time
    # print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x, y = parse2(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(x, y))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


