# EverybodyCodes - Echoes of Enigmatus - Quest 2

import os
import time
import re


IN_FILE1 = os.path.join("2025.6","inputs","2025.6-02.sample.txt")
# IN_FILE1 = os.path.join("2025.6","inputs","2025.6-02-1.txt")
# IN_FILE2 = os.path.join("2025.6","inputs","2025.6-02-2.txt")
# IN_FILE3 = os.path.join("2025.6","inputs","2025.6-02-3.txt")



def parse(IN_FILE):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    commands = list()
    for line in data:
        s = line.replace('[', ' ').replace(']', ' ').replace('=', ' ').replace(',', ' ')
        parts = s.split()
        parts = [p for p in parts if p not in ('id', 'left', 'right')]
        commands.append([parts[0], int(parts[1]), [int(parts[2]), parts[3]], [int(parts[4]), parts[5]]])

    return commands


# ['ADD', 1, [10, 'A'], [30, 'H']]

def add_node(t: dict, id: int, lft: list) -> dict:
    pass

def part1(data):     # => 
    l_tree = dict()
    r_tree = dict()

    # Build trees
    for command in data:
        cmd, id, lft, rgt = command
        
        # Left Tree
        if not l_tree:
            l_tree[id] = {'val':lft[0], 'data':lft[1]}
        else:
            add_node(l_tree, id, lft)

        # Right Tree
        if not r_tree:
            r_tree[id] = {'val':rgt[0], 'data':rgt[1]}
        else:
            add_node(r_tree, id, rgt)


    # widest level


    # concatenate data from that level


    # return the concatenated string

    return 0


def part2(data):     # => 

    return 
    

def part3(data):     # => 

    return 0


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(x))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


