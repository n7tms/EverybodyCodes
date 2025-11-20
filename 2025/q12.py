# EverybodyCodes - Quest 12

import os
import time


# IN_FILE2 = os.path.join("2025","inputs","2025-12.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-12-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-12-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-12-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    barrels = []
    for r, row in enumerate(data):
        b_row = []
        for c, col in enumerate(row):
            b_row.append(int(col))
        barrels.append(b_row)

    return barrels


def part1(data):           # => 239
    loc = [[0,0]]
    destroyed = [[0,0]]

    while loc:
        r,c = loc.pop()
        if c+1 < len(data[0]):
            if data[r][c+1] <= data[r][c]:
                if [r,c+1] not in destroyed:
                    destroyed.append([r,c+1])
                    loc.append([r,c+1])
        if r+1 < len(data):
            if data[r+1][c] <= data[r][c]:
                if [r+1,c] not in destroyed:
                    destroyed.append([r+1,c])
                    loc.append([r+1,c])
        if c-1 >= 0:
            if data[r][c-1] <= data[r][c]:
                if [r,c-1] not in destroyed:
                    destroyed.append([r,c-1])
                    loc.append([r,c-1])
        if r-1 >= 0:
            if data[r-1][c] <= data[r][c]:
                if [r-1,c] not in destroyed:
                    destroyed.append([r-1,c])
                    loc.append([r-1,c])
    
    return len(destroyed)



def part2(data):     # => 5594
    loc = [[0,0]]
    destroyed = [[0,0]]

    while loc:
        r,c = loc.pop()
        if c+1 < len(data[0]):
            if data[r][c+1] <= data[r][c]:
                if [r,c+1] not in destroyed:
                    destroyed.append([r,c+1])
                    loc.append([r,c+1])
        if r+1 < len(data):
            if data[r+1][c] <= data[r][c]:
                if [r+1,c] not in destroyed:
                    destroyed.append([r+1,c])
                    loc.append([r+1,c])
        if c-1 >= 0:
            if data[r][c-1] <= data[r][c]:
                if [r,c-1] not in destroyed:
                    destroyed.append([r,c-1])
                    loc.append([r,c-1])
        if r-1 >= 0:
            if data[r-1][c] <= data[r][c]:
                if [r-1,c] not in destroyed:
                    destroyed.append([r-1,c])
                    loc.append([r-1,c])


    loc = [[len(data)-1, len(data[0])-1]]
    while loc:
        r,c = loc.pop()
        if c+1 < len(data[0]):
            if data[r][c+1] <= data[r][c]:
                if [r,c+1] not in destroyed:
                    destroyed.append([r,c+1])
                    loc.append([r,c+1])
        if r+1 < len(data):
            if data[r+1][c] <= data[r][c]:
                if [r+1,c] not in destroyed:
                    destroyed.append([r+1,c])
                    loc.append([r+1,c])
        if c-1 >= 0:
            if data[r][c-1] <= data[r][c]:
                if [r,c-1] not in destroyed:
                    destroyed.append([r,c-1])
                    loc.append([r,c-1])
        if r-1 >= 0:
            if data[r-1][c] <= data[r][c]:
                if [r-1,c] not in destroyed:
                    destroyed.append([r-1,c])
                    loc.append([r-1,c])


    return len(destroyed)


def create_location_grid(data):
    grid = []
    for r, row in enumerate(data):
        for c, _ in enumerate(row):
            grid.append([r,c])
    return grid


def destroy_barrels(start, barrels) -> list:
    pass

def part3(data):           # => 4161 is the correct answer
    max_destroyed = 0

    # create a location map of all the barrels
    grid = create_location_grid(data)

    for loc in grid[:]:
        db = destroy_barrels(loc,data)
        if len(db) > max_destroyed:
            max_destroyed = len(db)
            destroyed_barrels = db.copy()
    
    



    

    return 0


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

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


