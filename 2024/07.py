# Everybody Codes: 07

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-07-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-07-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-07-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-07-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-07-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-07-3.txt")


def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    chariots = {}
    for line in data:
        c, actions = line.split(":")
        if c not in chariots:
            chariots[c] = {"Actions":actions.split(","), "Powers":[], "Total":0}
    return chariots
    

def part1(chariots):           # => GFDKAJIHB
    for chariot, data in chariots.items():
        pwr = 10
        actions = chariots[chariot]["Actions"]
        pwrs = []
        for x in range(10):
            action = actions[x % len(actions)]
            if action == "+":
                pwr += 1
            elif action == "-":
                pwr -= 1
            chariots[chariot]["Powers"].append(pwr)
        chariots[chariot]["Total"] = sum(chariots[chariot]["Powers"])
        
    # probably not the most efficient, but create a dictionary of just the chariots and total powers...
    totals = {}
    for c,d in chariots.items():
        totals[c] = d["Total"]
    
    # ... sort them, reverse them, and return them
    out = sorted(totals.items(), key=lambda item: item[1])
    out2 = [t[0] for t in out]
    out2.reverse()
    return ''.join(out2)


def part2(chariots):            # => 
    # DKEIBGJCH wrong
    # KDGBECJIH wrong
    # ?
    track = "-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=---=++==--+++==++=+=--==++==+++=++=+++=--=+=-=+=-+=-+=-+-=+=-=+=-+++=+==++++==---=+=+=-S"
    # track = "+===++-=+=-S"

    loops = 10
    for chariot, data in chariots.items():
        pwr = 10
        actions = chariots[chariot]["Actions"]

        for loop in range(loops):
            for s, segment in enumerate(track):
                action = actions[s % len(actions)] if track[s] in "=S" else track[s]
                if action == "+":
                    pwr += 1
                elif action == "-":
                    pwr -= 1 if pwr > 0 else 0 
                chariots[chariot]["Powers"].append(pwr)
        chariots[chariot]["Total"] = sum(chariots[chariot]["Powers"])
                
    # probably not the most efficient, but create a dictionary of just the chariots and total powers...
    totals = {}
    for c,d in chariots.items():
        totals[c] = d["Total"]
    
    # ... sort them, reverse them, and return them
    out = sorted(totals.items(), key=lambda item: item[1])
    out2 = [t[0] for t in out]
    out2.reverse()
    return ''.join(out2)



def part3(nails):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()