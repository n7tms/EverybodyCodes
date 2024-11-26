# Everybody Codes: 11

import numpy as np
import os
import time


# IN_FILE1 = os.path.join("2024","inputs","2024-11-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-11-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-11-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-11-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-11-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-11-3.txt")



def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    conversions = {}
    for line in data:
        termite,converts = line.split(":")
        convert = converts.split(",")
        conversions[termite] = convert
    
    return conversions

    

def part1(conversions, days):        # => 42
    population = ['A']

    for _ in range(days):
        new_population = []
        for termite in population:
            for term in conversions[termite]:
                new_population.append(term)
        population = new_population.copy()

    return len(population)



def part2(conversions, days):       # => 332461
    population = ['Z']

    for _ in range(days):
        new_population = []
        for termite in population:
            for term in conversions[termite]:
                new_population.append(term)
        population = new_population.copy()

    return len(population)


def part3(conversions, days):       # => 
    population_counts = []

    for k, _ in conversions.items():
        print(k,end=": ")
        population = [k]
        for day in range(days):
            print(day,end=" ")
            new_population = []
            for termite in population:
                for term in conversions[termite]:
                    new_population.append(term)
            population = new_population.copy()
        population_counts.append(len(population))
        print()
    
    population_counts.sort()
    difference = population_counts[-1] - population_counts[0]

    return len(population)




def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data, 4))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data,10))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3(data, 20))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()