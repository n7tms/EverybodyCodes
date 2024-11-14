# Everybody Codes: 03

import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-02-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-02-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-02-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-02-2.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-02-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-02-1.txt")


def parse():
    pass


def part1():
    pass


def part2():
    pass


def part3():
    pass




def solve():
    """Solve the puzzle for the given input."""
    words, inscription = parse1(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(words, inscription))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")


    words, inscription = parse1(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(words, inscription))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    words, inscription = parse1(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(words, inscription))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()