# Everybody Codes: 13

import numpy as np
import os
import time


IN_FILE1 = os.path.join("2024","inputs","2024-13-1.sample.txt")
# IN_FILE1 = os.path.join("2024","inputs","2024-13-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-13-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-13-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-13-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-13-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    start = (0,0)
    end = (0,0)
    maze = []
    for cell in data:
        row = []
        for c in cell:
            if c == "#":
                row.append(-1)
            elif c == 'S':
                start = (len(maze),len(row))
                row.append(0)
            elif c == 'E':
                end = (len(maze),len(row))
                row.append(0)
            else:
                row.append(int(c))
        maze.append(row)

    return maze, start, end
    

def part1():           # => 
    pass

def part2():            # => 
    pass

def part3():           # => 
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