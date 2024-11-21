# Everybody Codes: 13

import numpy as np
import os
import time
from collections import deque


IN_FILE1 = os.path.join("2024","inputs","2024-13-1.sample.txt")
# IN_FILE1 = os.path.join("2024","inputs","2024-13-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-13-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-13-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-13-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-13-3.txt")

def find_least_cost_path(maze, start, end):
    """Finds the least cost path in a maze using Dijkstra's algorithm."""

    # Define directions (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Create a cost matrix (initialize with infinity)
    cost = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
    cost[start[0]][start[1]] = 0

    # Create a queue for BFS
    queue = deque([(start, 0)])

    # Keep track of visited cells
    visited = set([start])

    while queue:
        (x, y), current_cost = queue.popleft()

        # Check if we reached the end
        if (x, y) == end:
            return current_cost

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if neighbor is valid
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:  #and (nx, ny) not in visited:
                # new_cost = current_cost + maze[nx][ny]
                new_cost = current_cost + (abs(maze[nx][ny] - maze[x][y])) + 1
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    queue.append(((nx, ny), new_cost))
                    visited.add((nx, ny))

    return -1  # No path found

def parse(IN_FILE):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    start = (0,0)
    end = (0,0)
    maze = []
    for cell in data:
        row = []
        for c in cell:
            if c == "#":
                row.append(float('inf'))
            elif c == 'S':
                start = (len(maze),len(row))
                row.append(0)
            elif c == 'E':
                end = (len(maze),len(row))
                row.append(0)
            else:
                row.append(int(c))
        maze.append(row)

    return maze, start, end
    

def part1(maze, start, end):           # => 
    return find_least_cost_path(maze,start,end)

def part2():            # => 
    pass

def part3():           # => 
    pass       



def solve():
    """Solve the puzzle for the given input."""
    data, s, e = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data, s, e))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    # start_time = time.time()
    # p2 = str(part2(data))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()