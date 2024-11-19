# Everybody Codes: 05

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-05-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-05-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-05-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-05-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-05-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-05-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    x = [line.split() for line in data]

    # convert all elements to ints
    y = [[int(item) for item in rw] for rw in x]

    # rotate the matrix CCW
    t = list(reversed(list(zip(*y))))
    t5 = [list(t0) for t0 in t]

    # return the matrix back to the program
    return t5
    

def part1(clappers, rounds):           # => 4223
    # start with last row
    # pop digit from front of row
    # clap
    #   if clapper =< row count, insert clapper into position (clapper - 1)
    #   if clapper > row count, insert clapper into position (clapper - row count)
    # print first digit in each row, from last to first.

    clapper_size = len(clappers)
    for rnd in range (1,rounds+1):
        # Determine head row
        r1 = rnd % clapper_size
        if r1 == 0:
            head_row = 0
            clap_row = clapper_size - 1
        else:
            head_row = clapper_size - r1
            clap_row = head_row - 1

        clapper = clappers[head_row].pop(0)
        if clapper > len(clappers[clap_row]):
            clappers[clap_row].insert(len(clappers[clap_row]) - (clapper - len(clappers[clap_row]))+1, clapper)
        else:
            clappers[clap_row].insert(clapper-1, clapper)
        
    # print first element from each row
    firsts = ""
    for rw in clappers:
        firsts = firsts + str(rw[0])
    return firsts[::-1]


def part2(clappers, rounds):            # => 20580403334550
    shouts = {}
    clapper_size = len(clappers)
    rnd = 0
    while True:
        rnd += 1
        # Determine head row
        r1 = rnd % clapper_size
        if r1 == 0:
            head_row = 0
            clap_row = clapper_size - 1
        else:
            head_row = clapper_size - r1
            clap_row = head_row - 1

        clapper = clappers[head_row].pop(0)
        if clapper > len(clappers[clap_row]):
            clappers[clap_row].insert(len(clappers[clap_row]) - (clapper - len(clappers[clap_row]))+1, clapper)
        else:
            clappers[clap_row].insert(clapper-1, clapper)
        
        # Add these first to dictionary
        firsts = ""
        for rw in range(len(clappers)-1,-1,-1):
            firsts = firsts + str(clappers[rw][0])
        # shout = firsts[::-1]
        shout = firsts

        if shout in shouts:
            shouts[shout] += 1
        else: 
            shouts[shout] = 1
        
        if shouts[shout] == rounds:
            return str(shout) + " " + str(rnd) + " " + str(int(shout) * rnd)
           



def part3(clappers, rounds):       # => 
    shouts = {}
    clapper_size = len(clappers)
    rnd = 0
    while True:
        rnd += 1
        # Determine head row
        r1 = rnd % clapper_size
        if r1 == 0:
            head_row = 0
            clap_row = clapper_size - 1
        else:
            head_row = clapper_size - r1
            clap_row = head_row - 1

        clapper = clappers[head_row].pop(0)
        if clapper > len(clappers[clap_row]):
            clappers[clap_row].insert(len(clappers[clap_row]) - (clapper - len(clappers[clap_row]))+1, clapper)
        else:
            clappers[clap_row].insert(clapper-1, clapper)
        
        # Add these first to dictionary
        firsts = ""
        for rw in range(len(clappers)-1,-1,-1):
            firsts = firsts + str(clappers[rw][0])
        # shout = firsts[::-1]
        shout = int(firsts)

        if shout in shouts:
            shouts[shout] += 1
        else: 
            shouts[shout] = 1
        
        if shouts[shout] == rounds:
            return max(shouts)
           



def solve():
    """Solve the puzzle for the given input."""
    # data = parse(IN_FILE1)
    # start_time = time.time()
    # p1 = str(part1(data, 10))
    # exec_time = time.time() - start_time
    # print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(data, 2024))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data, 10000000))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()