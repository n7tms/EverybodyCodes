# Everybody Codes: 12

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-12-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-12-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-12-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-12-2.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-12-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-12-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    launchers = []
    targets = []
    ground = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == 'A':
                launchers.append({(r,c):1})
            if col == 'B':
                launchers.append({(r,c):2})
            if col == 'C':
                launchers.append({(r,c):3})
            if col == 'T':
                targets.append((r,c))
            if col == 'H':
                targets.append((r,c))
                targets.append((r,c))
            if col == '=':
                ground = r
    return launchers, targets, ground

def parse3(IN_FILE):
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    launchers = [{(3,1):1},{(2,1):2},{(1,1):3}]
    ground = 4
    r_offset, c_offset = 3, 1
    meteors = []

    for meteor in data:
        mc, mr = meteor.split(" ")
        meteors.append((r_offset-int(mr), int(mc) + c_offset))

    return launchers, meteors, ground



def find_missile_power(launcher, target, ground):
    lr, lc = launcher
    tr, tc = target
    max_range = (tc - lc) // 2

    for power in range(1,max_range):
        # start the missile at the launcher
        mr, mc = lr, lc

        # upward diaganol trajectory
        for x in range(power):
            mr -= 1
            mc += 1
            if (mr, mc) == target:
                return power
            if mc > tc:
                return 0
    
        # horizantol trajectory
        for x in range(power):
            mc += 1
            if (mr, mc) == target:
                return power
            if mc > tc:
                return 0

        # downward diaganol trajectory
        while mr < ground and mc < tc:
            mr += 1
            mc += 1
            if (mr, mc) == target:
                return power

    return 0


def find_missile_power3(launcher, target, ground):
    lr, lc = launcher
    tr, tc = target
    max_range = (tc - lc) // 2
    lowest_power = 9999

    # implement time delay
    for time_delay in range(tc-lc):
        mtr = tr + time_delay
        mtc = tc - time_delay

        for power in range(1,max_range):
            # start the missile at the launcher
            mr, mc = lr, lc

            # upward diaganol trajectory
            for x in range(power):
                mr -= 1
                mc += 1
                mtr += 1
                mtc -= 1

                if (mr, mc) == (mtr, mtc):
                    lowest_power = power if power < lowest_power else lowest_power
                if mc > tc:
                    return 0
        
            # horizantol trajectory
            for x in range(power):
                mc += 1
                mtr += 1
                mtc -= 1
                if (mr, mc) == (mtr, mtc):
                    lowest_power = power if power < lowest_power else lowest_power
                if mc > tc:
                    return 0

            # downward diaganol trajectory
            while mr < ground and mc < tc:
                mr += 1
                mc += 1
                mtr += 1
                mtc -= 1
                if (mr, mc) == (mtr, mtc):
                    lowest_power = power if power < lowest_power else lowest_power

    if lowest_power == 9999: lowest_power = 0
    return lowest_power

def part1(launchers, targets, ground):           # => 180
    total_shooting_power = 0
    
    for t in targets:
        for l in launchers:
            k,v = next(iter(l.items()))
            power = find_missile_power(k,t, ground)
            if power > 0:
                total_shooting_power += v * power
    return total_shooting_power

def part2(nails):            # => 20490
    pass


def part3(launchers, meteors, ground):       # => 
    total_shooting_power = 0
    
    for t in meteors:
        for l in launchers:
            k,v = next(iter(l.items()))
            power = find_missile_power3(k,t, ground)
            if power > 0:
                total_shooting_power += v * power
    return total_shooting_power


def solve():
    """Solve the puzzle for the given input."""
    l, t, g = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(l, t, g))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    l,t,g = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part1(l,t,g))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    l,t,g = parse3(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(l,t,g))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()