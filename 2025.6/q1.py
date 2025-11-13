# EverybodyCodes - Echoes of Enigmatus - Quest 1

import os
import time
import re


# IN_FILE2 = os.path.join("2025.6","inputs","2025.6-01.sample.txt")
IN_FILE1 = os.path.join("2025.6","inputs","2025.6-01-1.txt")
IN_FILE2 = os.path.join("2025.6","inputs","2025.6-01-2.txt")
# IN_FILE3 = os.path.join("2025.6","inputs","2025.6-01-3.txt")



def parse(IN_FILE):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    eni_params = list()
    pattern = r'[A-Z]=(\d+)'
    for line in data:
        matches = re.findall(pattern, line)
        temp = list()
        temp.append([int(matches[0]), int(matches[3]), int(matches[6])])
        temp.append([int(matches[1]), int(matches[4]), int(matches[6])])
        temp.append([int(matches[2]), int(matches[5]), int(matches[6])])
        eni_params.append(temp)

    return eni_params


def eni_algo(n, e, m):
    score = 1
    remainders = list()
    for _ in range(e):
        score *= n
        rem = score % m
        remainders.insert(0,str(rem))
    
    return "".join(remainders)

def eni_algo2(n, e, m):

    memoized_rem = list()
    score = 1
    remainders = list()
    for _ in range(e):
        score *= n
        rem = score % m
        remainders.insert(0,rem)

        if remainders[:5] in memoized_rem:
            T = e
            n = _
            s = memoized_rem.index(remainders[:5])
            c = n - s
            correct = memoized_rem[s + (T - 1 - s) % c]
            break
        else:
            memoized_rem.append(remainders[:5].copy())
    
    if _+1 == e:
        correct = remainders[:5].copy()
       

    return "".join([str(r) for r in correct])




def part1(data):     # => 1099999998
    all_remainders = list()
    for params in data:
        remainders = 0
        for N, E, M in params:
            remainders += int(eni_algo(N,E,M))
        all_remainders.append(remainders)
    return max(all_remainders)


def part2(data):     # => 236309384189337
    all_remainders = list()
    for params in data:
        remainders = 0
        for N, E, M in params:
            remainders += int(eni_algo2(N,E,M))
        all_remainders.append(remainders)
    return max(all_remainders)
    

def part3(data):     # => 

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

    # x = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(x))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()


