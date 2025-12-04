# EverybodyCodes - Quest 17

import os
import time

DAY = 17

# IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}.sample.txt")
IN_FILE1 = os.path.join("2025","inputs",f"2025-{DAY}-1.txt")
IN_FILE2 = os.path.join("2025","inputs",f"2025-{DAY}-2.txt")
# IN_FILE3 = os.path.join("2025","inputs",f"2025-{DAY}-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    lava_flow = []
    volcano = []
    for r,line in enumerate(data):
        lava_line = []
        for c, cell in enumerate(line):
            if cell == "@": # the volcano
                volcano = [r,c]
                lava_line.append(0)
            else:
                lava_line.append(int(cell))
        lava_flow.append(lava_line)


    return volcano, lava_flow

def calc_in_flow(v: list, cell: list, value: int, radius: int) -> int:
    # if in the flow, return the value of the cell; otherwise return 0

    Xv, Yv = v
    Xc, Yc = cell

    if (((Xv-Xc)**2)+((Yv-Yc)**2)) <= radius ** 2:
        return value
    else:
        return 0


def calc_in_flow2(v: list, cell: list, value: int, radius: int) -> int:
    # if in the flow (but not in the previous flow), return the value of the cell; otherwise return 0

    Xv, Yv = v
    Xc, Yc = cell

    if (((Xv-Xc)**2)+((Yv-Yc)**2)) <= radius ** 2 and (((Xv-Xc)**2)+((Yv-Yc)**2)) > (radius-1) ** 2:
        return value
    else:
        return 0



def part1(volcano, lava_flow):     # => 1573
    damage = 0

    for r,line in enumerate(lava_flow):
        for c,cell in enumerate(line):
            damage += calc_in_flow(volcano, [r,c], cell, 10)

    return damage


def part2(volcano, lava_flow):     # => 67275
    greatest_damage = [0,0]

    for radius in range(len(lava_flow)//2):
        damage = 0
        for r,line in enumerate(lava_flow):
            for c,cell in enumerate(line):
                d = calc_in_flow2(volcano, [r,c], cell, radius)
                if d>0:
                    # print(f"[{r},{c}]: {cell}")
                    damage += d
        if damage > greatest_damage[0]:
            greatest_damage = [damage, radius]

    return greatest_damage[0] * greatest_damage[1]



def part3(data):     # => 

    return 0


def solve():
    """Solve the puzzle for the given input."""
    v,l = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(v,l))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    v,l = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(v,l))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


