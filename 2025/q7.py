# EverybodyCodes - Quest 7

import os
import time


IN_FILE3 = os.path.join("2025","inputs","2025-07.sample.txt")
IN_FILE1 = os.path.join("2025","inputs","2025-07-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-07-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-07-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().split("\n\n")

    # data[0] are the names
    # data[1] are the rules
    names = data[0].split(",")
    rules = dict()
    for line in data[1].splitlines():
        firsts, seconds = line.split(" > ")
        rules[firsts] = seconds.split(",")

    return names, rules


def match(name: str, rules: dict) -> bool:

    pairs = [name[i:i+2] for i in range(len(name)-1)]
    for f,s in pairs:
        if f in rules:
            if s in rules[f]:
                continue
        return False
    return True


def find_words(current: str, min_len: int, max_len: int, result: set, next_letters):
    if len(current) > max_len:
        return
    if min_len <= len(current) <= max_len:
        result.add(current)

    last = current[-1]
    if last not in next_letters:
        return
    for nxt in next_letters[last]:
        find_words(current + nxt, min_len, max_len, result, next_letters)


def part1(names, rules):           # => Azardith
    for name in names:
        if match(name, rules):
            return name



    return "no matches found."


def part2(names, rules):     # => 3128
    idx_sum = 0
    for idx, name in enumerate(names):
        if match(name, rules):
            idx_sum += (idx+1)
    return idx_sum
    

def part3(names, rules):           # => 

    total_found = 0
    for name in names:
        if not match(name, rules):
            continue
        
        words = set()
        find_words(name, 7, 11, words, rules)

        print(f"{name}: Found {len(words)} distinct words (length 7-11):")
        total_found += len(words)
    
    return total_found


def solve():
    """Solve the puzzle for the given input."""
    n, r = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(n, r))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    n, r = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(n, r))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    n, r = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(n, r))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


