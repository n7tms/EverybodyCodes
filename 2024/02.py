# Everybody Codes: 02

import os
import time
from collections import defaultdict

# IN_FILE1 = os.path.join("2024","inputs","2024-02-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-02-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-02-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-02-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-02-1.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-02-1.txt")

def parse1(IN_FILE):
    """
    Parse
    """
    # aoc.get_input(2023,7,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n\n")

    words = data[0].split(":")
    words = words[1].split(",")

    inscription = data[1]

    return words,inscription


def part1(w,i):        # => 33
    """
    Solve part 1
    
    """
    runic_words = 0
    for word in w:
        runic_words += i.count(word)

    return runic_words



def part2(w,i):        # => 5139
    """
    Solve part 2
    
    """
    
    inscriptions = i.splitlines()
    runic_symbols = 0

    w += [x[::-1] for x in w if len(x) > 1]


    for inscription in inscriptions:
        runics = 0
        last = 0
        fnd = [0] * len(inscription)
        for j in range(0,len(inscription)):
            for word in w:
                cmp = "".join(inscription[j:j+len(word)])
                if cmp == word:
                    for k in range(j, j+len(word)):
                        fnd[k] = 1
            
        runics = sum(fnd)

        # print(inscription + ": " + str(runics))
        # fnd.clear()
        runic_symbols += runics
        
    return runic_symbols
            
    
    



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



if __name__ == "__main__":
    solve()