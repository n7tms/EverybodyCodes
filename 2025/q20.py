# EverybodyCodes - Quest 20

import os
import time

DAY = 20

# IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
# IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    maze = []
    for line in data:
        maze_line = []
        for ch in line:
            maze_line.append(ch)
        maze.append(maze_line)

    return maze


def part1(data):     # => 131

    trampolines = 0

    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == "T": # this is a trampoline; check for neighbors.
                # check right (no need to check left)
                if c < len(line)-1 and line[c+1] == "T":
                    trampolines += 1
                # if r is even and c is odd, check down
                if r % 2 == 0 and c % 2 != 0 and r < len(data)-1 and data[r+1][c] == "T":
                    trampolines += 1
               
                # if r is odd and c is even, check down
                if r % 2 != 0 and c % 2 == 0 and r < len(data)-1 and data[r+1][c] == "T":
                    trampolines +=1
                
    return trampolines



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


