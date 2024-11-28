# Everybody Codes: 18

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-18-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-18-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-18-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-18-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-18-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-18-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    palm_trees = []
    starts = []
    farm_paths = []
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if (c == 0 or c == len(row)-1) and col == '.':
                starts.append((r,c))
            elif col == '.':
                farm_paths.append((r,c))
            elif col == 'P':
                farm_paths.append((r,c))
                palm_trees.append((r,c))
    
    return palm_trees, starts, farm_paths


def part1(palms, starts, paths):           # => 119
    water_locations = set()
    
    # add the start locations to the water_locations
    for x in starts:
        water_locations.add(x)
    
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    turns = 0
    while palms:
        turns += 1
        new_water_locations = set()
        for wl in water_locations:
            for d in directions:
                temp = (wl[0] + d[0], wl[1] + d[1])
                if temp in paths:
                    new_water_locations.add(temp)
                    paths.remove(temp)


                    if temp in palms:
                        palms.remove(temp)

        # water_locations = water_locations.union(new_water_locations)
        water_locations = new_water_locations.copy()

    return turns

def part2(data):            # => 1641
    pass


def part3(palms, paths):       # => 226331 (brute force; took a while!)
    potential_wells = set(paths) - set(palms)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    minimum_time = float('inf')
    recorded_times = {}

    for well in potential_wells:
        water_locations = set()
        water_locations.add(well)
        tmp_palms = palms.copy()
        tmp_paths = paths.copy()

        recv_water = 0

        turns = 0
        while tmp_palms:
            turns += 1
            new_water_locations = set()
            for wl in water_locations:
                for d in directions:
                    temp = (wl[0] + d[0], wl[1] + d[1])
                    if temp in tmp_paths:
                        new_water_locations.add(temp)
                        tmp_paths.remove(temp)


                        if temp in tmp_palms:
                            tmp_palms.remove(temp)
                            recv_water += turns

            # water_locations = water_locations.union(new_water_locations)
            water_locations = new_water_locations.copy()
            if recv_water > minimum_time: break

        
        minimum_time = recv_water if recv_water < minimum_time else minimum_time
        recorded_times[well] = recv_water
        print(f"well: {well}, time: {recv_water}, min so far: {minimum_time}")

    
    return minimum_time


def solve():
    """Solve the puzzle for the given input."""
    p,s,f = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(p,s,f))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # p,s,f = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part1(p,s,f))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    p,s,f = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(p,f))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()