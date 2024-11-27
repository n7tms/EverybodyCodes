# Everybody Codes: 16

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-16-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-16-1.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-16-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-16-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-16-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-16-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    positions, cat_faces = data[0], data[2:]
    pulls = [int(x) for x in positions.split(',')]

    wheels = {}
    for x in range(len(pulls)):
        wheels[x] = {'faces':[], 'spins':pulls[x]}
    
    for line in cat_faces:
        index = 0
        wheel = 0
        while index < len(line):
            if line[index] != ' ':
                face = line[index:index+3]
                wheels[wheel]['faces'].append(face)
            index += 4
            wheel += 1

    return wheels


def part1(wheels):           # => <:- ^_^ <:< <.> 

    wheel_index = [0]*len(wheels)

    for cnt in range(100):
        for wheel, data in wheels.items():
            faces, spins = data['faces'], data['spins']
            wheel_index[wheel] += spins
    
    resulting_face = ''
    for w, d in wheels.items():
        faces = wheels[w]['faces']
        resulting_face = resulting_face + faces[wheel_index[w] % len(faces)] + ' '
    return resulting_face



def part2(wheels):            # => 
    wheel_index = [0]*len(wheels)
    total_byte_coin = 0

    for cnt in range(202420242024):
        for wheel, data in wheels.items():
            faces, spins = data['faces'], data['spins']
            wheel_index[wheel] += spins
    
        resulting_face = ''
        for w, d in wheels.items():
            faces = wheels[w]['faces']
            resulting_face = resulting_face + faces[wheel_index[w] % len(faces)]
        # print(resulting_face)

        # Extracting just the eyes
        eye_pos = [0, 2, 3, 5, 6, 8, 9, 11]
        extracted_characters = [resulting_face[i] for i in eye_pos if i < len(resulting_face)]

        # Counting each character
        character_counts = {}
        for char in extracted_characters:
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1

        for _, v in character_counts.items():
            if v > 2:
                total_byte_coin += 1 + (v-3)

    return total_byte_coin


def part3(data):       # => 
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