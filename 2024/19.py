# Everybody Codes: 19

import numpy as np
import os
import time
import copy

# IN_FILE1 = os.path.join("2024","inputs","2024-19-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-19-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-19-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-19-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-19-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-19-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        rotations, rest = fp.read().split('\n\n')

    lines = rest.splitlines()
    hidden_message = []
    for l in lines:
        tmp = [x for x in l]
        hidden_message.append(tmp)

    return rotations, hidden_message

# 
rotate_left = {(-1,-1):(0,-1), (-1,0):(-1,-1), (-1,1):(-1,0), (0,-1):(1,-1), (0,1):(-1,1), (1,-1):(1,0), (1,0):(1,1), (1,1):(0,1), (0,0):(0,0)}
rotate_right = {(-1,-1):(-1,0), (-1,0):(-1,1), (-1,1):(0,1), (0,-1):(-1,-1), (0,1):(1,1), (1,-1):(0,-1), (1,0):(1,-1), (1,1):(1,0), (0,0):(0,0)}
neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def left_rotation(block, rotation_point):
    rotated_block = copy.deepcopy(block)
    rpr, rpc = rotation_point
    for neighbor in neighbors:
        nr, nc = neighbor
        rr, rc = rotate_left[(nr,nc)][0], rotate_left[(nr,nc)][1]
        new_char = block[rpr+nr][rpc+nc]
        rotated_block[rpr+rr][rpc+rc] = new_char
    
    return rotated_block

def right_rotation(block, rotation_point):
    rotated_block = copy.deepcopy(block)
    rpr, rpc = rotation_point
    for neighbor in neighbors:
        nr, nc = neighbor
        rr, rc = rotate_right[(nr,nc)][0], rotate_right[(nr,nc)][1]
        new_char = block[rpr+nr][rpc+nc]
        rotated_block[rpr+rr][rpc+rc] = new_char
    
    return rotated_block


def find_message(block):
    message = ''
    in_message = False
    for r in range(len(block)):
        for c in range(len(block[1])):
            if block[r][c] == '<': return message
            if in_message: message = message + block[r][c]
            if block[r][c] == '>': in_message = True
    return message
            

def part1(rotations, hidden_message):           # => 6948379425631369

    rot_index = 0
    for r in range(1,len(hidden_message)-1):
        for c in range(1,len(hidden_message[1])-1):
            idx = rot_index % len(rotations)
            if rotations[idx] == 'L':
                hidden_message = left_rotation(hidden_message, (r,c))
            else:
                hidden_message = right_rotation(hidden_message, (r,c))

            rot_index += 1
    
    return find_message(hidden_message)


def part2(rotations, hidden_message, rounds):            # => 9345391356337546
    for rnd in range(rounds):
        print(rnd, end=" ")
        rot_index = 0
        for r in range(1,len(hidden_message)-1):
            for c in range(1,len(hidden_message[1])-1):
                idx = rot_index % len(rotations)
                if rotations[idx] == 'L':
                    hidden_message = left_rotation(hidden_message, (r,c))
                else:
                    hidden_message = right_rotation(hidden_message, (r,c))

                rot_index += 1
    
    return find_message(hidden_message)


def part3(data):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    r,h = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(r,h))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # r,h = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(r,h, 100))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    r,h = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part2(r,h,1048576000))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()