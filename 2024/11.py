# Everybody Codes: 11

import numpy as np
import os
import time
from collections import Counter


IN_FILE1 = os.path.join("2024","inputs","2024-11-1.sample.txt")
# IN_FILE1 = os.path.join("2024","inputs","2024-11-1.txt")
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

# parseb and grow come from:
# https://topaz.github.io/paste/#XQAAAQD7AgAAAAAAAAAzHIoib6pXbueH4X9F244lVRDcOZab5q16fMXrmVEJ6+PP0gJsdiVImopcoOr3c2hN9Bn2BbLIeo1oMQQcqYIHFpKxG+om7Jm+enh6p2CX8DNgbxI9FwIy23wQNRqUx86N3kk/UgkttXjjOnuVe/DADcXNWk4wMDJqFasqJyTcJnHZdPPdG6WkNDTnj114yfDE/MPZ+N14Uu6A/Fa6+tu8rn9hRuQlexH4Bv8JrClA4bsC0/3BeqzEmlUkGlLy7TQEsagOr+wx2TBwBzFntq8AqR5eS53DHomqbuQlxA0CxTDXhcGPL56g9liK+AMPzs3osFm3KHOI6ldFs8GlvH+YsT9I4uNBbRLSVdRxJnqLIlWQJeLHUiEb2ffFzDzFc0ptkIPR6HpqVxEIYl9KZ0Pztz+svhZI7cCk2aGyaksFQRPvOpPO4wfUq8t1MjdcrM8OZ4ZPIDP9kIum2HUksUjnzRf/n37DzA==
def parseb(IN_FILE):
    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    conversions = {}
    for line in data:
        start, into = line.split(":")
        conversions[start] = Counter(into.split(","))
    return conversions


def grow(conversions, start, days):    
    cur = Counter({start: 1})
    for i in range(days):
        new = Counter()
        for a, acount in cur.items():
            for b, bcount in conversions[a].items():
                new[b] += acount*bcount
        cur = new
    return sum(cur.values())


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

def updateTermites(currentState, collectionOfTermites):
    newCurrentState={x:0 for x in collectionOfTermites.keys()}

    for sourceTermite, numberTermites in currentState.items():
        for newborn in collectionOfTermites[sourceTermite]:
            newCurrentState[newborn]=newCurrentState[newborn]+numberTermites
    return newCurrentState

def part3b(collectionOfTermites):   # => 738270514446
    # from: https://github.com/Torfab/adventOfCode2022/blob/main/everybodycodes/q11.py
    results={}
    for element in collectionOfTermites.keys():
        current={element:1}
        for _ in range(20):
            current=updateTermites(current, collectionOfTermites)
        results[element]=sum(current.values())
    return max(results.values())-min(results.values())


def solve():
    """Solve the puzzle for the given input."""
    # data = parse(IN_FILE1)
    data = parseb(IN_FILE1)
    start_time = time.time()
    # p1 = str(part1(data, 4))
    p1 = str(grow(data,"A",4))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(data,10))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part3b(data))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()