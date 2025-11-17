# EverybodyCodes - Quest 11

import os
import time


# IN_FILE2 = os.path.join("2025","inputs","2025-11.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-11-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-11-2.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-11-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    cols = [int(c) for c in data]

    return cols




def part1(data):           # => 302

    rounds = 0
    checksum = 0

    # phase 1
    moved = True
    while moved:
        rounds += 1
        moved = False
        for i, _ in enumerate(data):
            if i+1 >= len(data): break
            if data[i] > data[i+1]:
                data[i] -= 1
                data[i+1] += 1
                moved = True
        print(f"{rounds}: {data}")
    
    rounds -= 1

    # phase 2
    moved = True
    while moved:
        rounds += 1
        moved = False
        for i, _ in enumerate(data):
            if i+1 >= len(data): break
            if data[i] < data[i+1]:
                data[i] += 1
                data[i+1] -= 1
                moved = True
        print(f"{rounds}: {data}")

        if rounds == 10:
            break


    # calculate checksum
    checksum = 0
    for i,d in enumerate(data):
        checksum += ((i+1) * d)

    return checksum


def part2(data):     # => 3887051

    rounds = 0
    checksum = 0

    # phase 1
    moved = True
    while moved:
        rounds += 1
        moved = False
        for i, _ in enumerate(data):
            if i+1 >= len(data): break
            if data[i] > data[i+1]:
                data[i] -= 1
                data[i+1] += 1
                moved = True
        # print(f"{rounds}: {data}")
    
    rounds -= 1



    # phase 2
    moved = True
    while moved:
        rounds += 1
        moved = False
        for i, _ in enumerate(data):
            if i+1 >= len(data): break
            if data[i] < data[i+1]:
                data[i] += 1
                data[i+1] -= 1
                moved = True
        # print(f"{rounds}: {data}")


    return rounds-1

    

def part3(data):           # => 

    return 0


def solve():
    """Solve the puzzle for the given input."""
    x = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    x = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    x = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


