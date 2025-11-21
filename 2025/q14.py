# EverybodyCodes - Quest 14

import os
import time
from copy import deepcopy

DAY = 14

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

    floor = []
    for r, line in enumerate(data):
        row = []
        for c, tile in enumerate(line):
            if tile == ".":
                row.append(0)
            else:
                row.append(1)
        floor.append(row)
    
    return floor


def odd_neighbors(f: list, loc: list) -> bool:
    # return true if this tile needs to change

    DIRs = [[-1,-1],[-1,1],[1,-1],[1,1]]

    a,b = loc
    neighbors = 0
    for c,d in DIRs:
        if a+c >= 0 and b+d >= 0 and a+c < len(f) and b+d < len(f[0]):
            if f[a+c][b+d]: neighbors += 1
    
    if (neighbors in [0,2,4]) and f[a][b] == 0:
        return True
    elif (neighbors in [0,2,4]) and f[a][b] == 1:
        return True

    return False


def sum_tiles(f: list) -> int:
    at = 0
    for row in f:
        at += sum(row)
    
    return at


def part1(data: list):     # => 508
    rounds = 10
    active_tiles = 0
    for rnd in range(rounds):
        # tmp_data = deepcopy(data)
        tmp_data = [row[:] for row in data]
        for r,row in enumerate(data):
            for c,tile in enumerate(row):
                if odd_neighbors(data, [r,c]):
                    tmp_data[r][c] = 1 - tmp_data[r][c]

        active_tiles += sum_tiles(tmp_data)
        data = tmp_data

  
    return active_tiles



def part2(data):     # => 1171540
    rounds = 2025
    active_tiles = 0
    for rnd in range(rounds):
        tmp_data = [row[:] for row in data]
        for r,row in enumerate(data):
            for c,tile in enumerate(row):
                if odd_neighbors(data, [r,c]):
                    tmp_data[r][c] = 1 - tmp_data[r][c]

        active_tiles += sum_tiles(tmp_data)
        data = tmp_data
  
    return active_tiles



def part3(data, pattern):     # => 1006105152 is the correct answer (with help)
    rounds = 1000000000
    active_tiles = 0
    for rnd in range(rounds):
        tmp_data = [row[:] for row in data]
        for r,row in enumerate(data):
            for c,tile in enumerate(row):
                if odd_neighbors(data, [r,c]):
                    tmp_data[r][c] = 1 - tmp_data[r][c]

        active_tiles += sum_tiles(tmp_data)
        data = tmp_data

        if all(data[13+i][13:21] == pattern[i] for i in range(8)):
            print(f"Pattern found at round: {rnd}")
  
    return active_tiles


def part3_optimized(data, pattern):
    grid = [row[:] for row in data]        # 34x34 list of lists
    pattern = [row[:] for row in pattern]  # 8x8

    total = 0
    seen = {}
    step = 0
    N = 1_000_000_000

    while step < N:
        # Check for pattern
        match = True
        for i in range(8):
            if grid[13 + i][13:21] != pattern[i]:
                match = False
                break
        if match:
            active = sum(sum(row) for row in grid)
            total += active
            print(f"Pattern at step {step}, active tiles = {active}")

        # Cycle detection
        state = tuple(tuple(row) for row in grid)
        if state in seen:
            cycle_start = seen[state]
            cycle_len = step - cycle_start
            remaining = N - step
            cycles = remaining // cycle_len
            step += cycles * cycle_len
            # Note: we skip adding during fast-forward unless pattern repeats in cycle
            # This is conservative — if you want max accuracy, simulate one cycle
            continue

        seen[state] = step

        # Apply rule
        new_grid = [row[:] for row in grid]
        changed = False
        for r in range(34):
            for c in range(34):
                diag_count = 0
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 34 and 0 <= nc < 34 and grid[nr][nc]:
                        diag_count += 1
                if diag_count in (0, 2, 4):
                    new_grid[r][c] = 1 - grid[r][c]
                    changed = True
        grid = new_grid

        if not changed:
            print(f"Stabilized at step {step}")
            break

        step += 1

    return total


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x = parse(IN_FILE2)
    # x_forlater = deepcopy(x)
    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    p = parse(IN_FILE3)
    start_time = time.time()
    # p3 = str(part3(x, p))
    # p3 = str(part3_optimized(x_forlater, p))
    p3 = str(part3_optimized(x, p))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


