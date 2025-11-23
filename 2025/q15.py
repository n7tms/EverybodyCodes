# EverybodyCodes - Quest 15

import os
import time


DAY = 15

# IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    directions = data[0].split(",")

    return directions


from collections import deque

def part1(data):    # -> 128
    r = c = 0
    idx = 0
    facing = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U R D L

    positions = [(0, 0)]  # all turtle positions including start and end

    for move in data:
        turn, steps = move[0], int(move[1:])
        idx = (idx + (1 if turn == 'R' else -1)) % 4
        dr, dc = facing[idx]
        for _ in range(steps):
            r += dr
            c += dc
            positions.append((r, c))

    # === WALLS = all positions EXCEPT the final one ===
    walls = set(positions[:-1])   # ← critical line!
    start = (0, 0)
    end = positions[-1]

    # === Optional: bounding box (still helps a lot) ===
    all_r = [p[0] for p in positions]
    all_c = [p[1] for p in positions]
    min_r, max_r = min(all_r) - 5, max(all_r) + 5
    min_c, max_c = min(all_c) - 5, max(all_c) + 5

    for row in range(min_r, max_r + 1):
        walls.add((row, min_c))
        walls.add((row, max_c))
    for col in range(min_c + 1, max_c):  # avoid corners double-add
        walls.add((min_r, col))
        walls.add((max_r, col))

    # === BFS ===
    queue = deque([(0, 0, 0)])  # r, c, dist
    visited = set([(0, 0)])

    while queue:
        cr, cc, dist = queue.popleft()
        if (cr, cc) == end:
            return dist

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if (nr, nc) not in walls and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return "no path"


def part2(data):     # => 3805

    return part1(data)



def part3(data):
    # First pass: find goal and bounds
    r = c = idx = 0
    facing = [(-1,0),(0,1),(1,0),(0,-1)]
    min_r = max_r = min_c = max_c = 0

    for move in data:
        turn, steps = move[0], int(move[1:])
        idx = (idx + (1 if turn == 'R' else -1)) % 4
        dr, dc = facing[idx]
        r += dr * steps
        c += dc * steps
        min_r = min(min_r, r); max_r = max(max_r, r)
        min_c = min(min_c, c); max_c = max(max_c, c)
    goal = (r, c)

    # Reset and trace walls — but use a set with hashable tuples
    walls = set()
    r = c = 0
    idx = 0

    for move in data:
        turn, steps = move[0], int(move[1:])
        idx = (idx + (1 if turn == 'R' else -1)) % 4
        dr, dc = facing[idx]
        for _ in range(steps):
            r += dr
            c += dc
            if (r, c) != goal:  # don't block goal
                walls.add((r, c))

    # Add tight bounding box
    PAD = 2
    for row in range(min_r - PAD, max_r + PAD + 1):
        walls.add((row, min_c - PAD))
        walls.add((row, max_c + PAD))
    for col in range(min_c - PAD, max_c + PAD + 1):
        walls.add((min_r - PAD, col))
        walls.add((max_r + PAD, col))

    # BFS
    q = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while q:
        cr, cc, d = q.popleft()
        if (cr, cc) == goal:
            return d
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = cr + dr, cc + dc
            if (nr, nc) not in walls and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    x = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(x))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


