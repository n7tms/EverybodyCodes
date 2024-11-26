# Everybody Codes: 09

import numpy as np
import os
import time
from collections import deque


# IN_FILE1 = os.path.join("2024","inputs","2024-09-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-09-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-09-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-09-2.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-09-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-09-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    notes = [int(n) for n in data]
    return notes
    

def part1(notes, stamps):       # => 13127
    
    beetles = 0

    for n in notes:
        n1 = n
        for s in stamps:
            if n1 < s: continue
            # n // s
            # n % s
            beetles += n1 // s
            n1 = n1 % s

    return beetles


def part2(targets, terms):       # => 5233
    """
    Find the least number of terms that sum to the target using BFS.
    """
    beetles = 0
    for target in targets:
        terms.sort(reverse=True)  # Sorting helps reduce unnecessary computations
        queue = deque([(0, 0)])  # (current_sum, term_count)
        visited = set([0])  # To avoid revisiting sums

        while queue:
            current_sum, count = queue.popleft()

            # Check if we've reached the target
            if current_sum == target:
                beetles += count
            else:
                # Try adding each term
                for term in terms:
                    new_sum = current_sum + term
                    if new_sum <= target and new_sum not in visited:
                        visited.add(new_sum)
                        queue.append((new_sum, count + 1))
    return beetles

def part3(nails):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data, [10, 5, 3, 1]))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(IN_FILE2)
    start_time = time.time()
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    p2 = str(part2(data,stamps))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    data = parse(IN_FILE3)
    start_time = time.time()
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    p3 = str(part3(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()