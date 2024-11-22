# Everybody Codes: 14

import os
import time
import re

# IN_FILE1 = os.path.join("2024","inputs","2024-14-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-14-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-14-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-14-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-14-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-14-1.txt")

def parse1(IN_FILE):
    """
    Parse
    """
    # aoc.get_input(2023,7,False)

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    plan = []
    for line in data:
        plan.append(line.split(","))
    return plan


def part1(plan):        # => 155
    """
    Solve part 1
    
    """
    maxheight = 0
    curheight = 0
    plant = set()
    for cmd in plan[0]:
        match = re.match(r"([UDLFBR])(\d+)", cmd, re.IGNORECASE)
        if match:
            dir = match.group(1)
            mag = int(match.group(2))
        if dir == "U":
            curheight += mag
            if curheight > maxheight:
                maxheight = curheight
        if dir == "D":
            curheight -= mag
    
    return maxheight




def part2(plans):        # => 4995
    """
    Solve part 2
    
    """
    garden = set()
    for plan in plans:
        w,h,d = 0,0,0
        for cmd in plan:
            match = re.match(r"([UDLFBR])(\d+)", cmd, re.IGNORECASE)
            if match:
                dir = match.group(1)
                mag = int(match.group(2))

                if dir == "U":
                    for _ in range(mag):
                        h += 1
                        garden.add((w,h,d))
                if dir == "D":
                    for _ in range(mag):
                        h -= 1
                        garden.add((w,h,d))
                if dir == "L":
                    for _ in range(mag):
                        w -= 1
                        garden.add((w,h,d))
                if dir == "R":
                    for _ in range(mag):
                        w += 1
                        garden.add((w,h,d))
                if dir == "B":
                    for _ in range(mag):
                        d -= 1
                        garden.add((w,h,d))
                if dir == "F":
                    for _ in range(mag):
                        d += 1
                        garden.add((w,h,d))

    return len(garden)
            
    
def part3(plan):        # => 
    pass

    


def solve():
    """Solve the puzzle for the given input."""
    data = parse1(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")


    data = parse1(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse1(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()