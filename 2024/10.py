# Everybody Codes: 10

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-10-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-10-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-10-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-10-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-10-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-10-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    grid = []
    for d in data:
        g = [x for x in d]
        grid.append(g)
    return grid

def parse2(IN_FILE):
    """
    Parse for part 2
    """

    with open(IN_FILE) as fp:
        data = fp.read().split('\n\n')
    
    grids= []
    for lines in data:
        a = lines.split('\n')
        d = [x.split(' ') for x in a]
        f = [list(e) for e in zip(*d)]

        for g in f:
            grids.append(g)

    return grids
    


def find_letter(row,col,grid):
    col_letters = set()
    row_letters = set()

    # column letters
    for r in range(len(grid)):
        if grid[r][col] not in '*.':
            col_letters.add(grid[r][col])
    
    # row letters
    for c in range(len(grid[row])):
        if grid[row][c] not in '*.':
            row_letters.add(grid[row][c])
    
    letter = col_letters & row_letters
    letter = ''.join(letter)
    return letter


def calculate_power(runic_word):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    sop = 0
    for pos, rw in enumerate(runic_word):
        sop += ((letters.index(rw)+1) * (pos+1))

    return sop


def part1(grid):           # => ZNDFQKMGSTLJVHXW
    runic_word = ''

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == '.':
                runic_word = runic_word + find_letter(r,c,grid)


    return runic_word



def part2(grids):            # => 198124
    sum_of_powers = 0

    for grid in grids:
        runic_word = ''
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == '.':
                    runic_word = runic_word + find_letter(r,c,grid)
        sum_of_powers += calculate_power(runic_word)

    return sum_of_powers


def part3(nails):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse2(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()