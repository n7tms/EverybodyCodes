# EverybodyCodes - Quest 6

import os
import time
# import string


# IN_FILE3 = os.path.join("2025","inputs","2025-06.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-06-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-06-2.sample.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-06-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-06.sample.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-06-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    i_data = [d for d in data[0]]

    return i_data



def part1(professions):           # => 187
    # just count the swordsmen ('Aa')
    categories = dict()
    pairs = 0
    for p in professions:
        if p=="A" or p=="a":
            if p.isupper():
                if p in categories:
                    categories[p] += 1
                else:
                    categories[p] = 1
            else:
                if p.upper() in categories:
                    pairs += categories[p.upper()]

    return pairs


def part2(professions):     # => 3490
    # count everyone
    categories = dict()
    pairs = 0
    for p in professions:
        if p.isupper():
            if p in categories:
                categories[p] += 1
            else:
                categories[p] = 1
        else:
            if p.upper() in categories:
                pairs += categories[p.upper()]

    return pairs
    

def part3(professions):           # => 1667582509
    # copy the input string 1000 times.
    # then count all the mentors within 1000 either way of a knight

    # NOTE: This brute-force method takes about ~70 seconds to run.

    all_professions = professions * 1000
    dist = 1000

    mentors = 0
    for idx, prof in enumerate(all_professions):
        if prof.islower():
            # if the current knight (idx) is "near" the beginning, set the lower limit (lwr) to 0
            if idx < dist:
                lwr = 0
            else:
                lwr = idx-dist
            
            # if the current knight (idx) is "near" the end, set the upper limit (upr) to the end.
            if idx+dist > len(all_professions):
                upr = len(all_professions)
            else:
                upr = idx+dist+1

            # count the number of mentors that appear within that range (lwr to upr)
            mentors += all_professions[lwr:upr].count(prof.upper())
    return mentors


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

    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


