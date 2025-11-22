# EverybodyCodes - Quest 15

import os
import time
from heapq import heappush, heappop


DAY = 15

IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
# IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    directions = data[0].split(",")

    return directions


def part1(data):     # => 
    r, c = 0, 0

    walls = set()    
    facing = [(-1,0),(0,1),(1,0),(0,-1)]      # 0=up; 1=right; 2=down; 3=left
    idx = 0

    for dir in data:
        d,m = dir[0], int(dir[1:])

        if d == "R": 
            idx = (idx + 1) % 4
        else:
            idx = (idx - 1) % 4
        
        dr, dc = facing[idx]
        for _ in range(m):
            r += dr
            c += dc
            walls.add((r,c))


    start = (0, 0)
    goal  = (r, c)

    # A* priority queue: (f_score, g_score, row, col)
    open_set = []
    heappush(open_set, (abs(r) + abs(c), 0, 0, 0))   # f = h, g = 0

    came_from = {}
    g_score   = {start: 0}
    # We do NOT use a global visited set!
    # In A* on a grid with unit costs we can re-open nodes if a better path is found.

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while open_set:
        f, g, cr, cc = heappop(open_set)
        pos = (cr, cc)

        if pos == goal:
            return g                                    # this is the answer

        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            neighbor = (nr, nc)

            if neighbor in walls:
                continue

            tentative_g = g + 1

            if tentative_g < g_score.get(neighbor, float('inf')):
                # Better path found → record it
                came_from[neighbor] = pos
                g_score[neighbor] = tentative_g
                h = abs(nr - goal[0]) + abs(nc - goal[1])
                f_new = tentative_g + h
                heappush(open_set, (f_new, tentative_g, nr, nc))

    return "no path"



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


