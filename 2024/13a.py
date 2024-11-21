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
    

import heapq

def parse_maze(file_path):
    with open(file_path, 'r') as f:
        maze = [line.strip() for line in f.readlines()]
    
    rows, cols = len(maze), len(maze[0])
    adjacency_list = {}

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                        if maze[nr][nc] in "SE":
                            neighbors.append(((nr, nc), 0))
                        else:
                            neighbors.append(((nr, nc), int(maze[nr][nc])))
                adjacency_list[(r, c)] = neighbors

    return adjacency_list

def dijkstra(adjacency_list, start, end):
    # Priority queue: (cost, node)
    pq = [(0, start)]
    visited = set()
    distances = {start: 0}
    previous = {}

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue

        visited.add(current_node)

        # Stop if we reached the end node
        if current_node == end:
            break

        for neighbor, weight in adjacency_list.get(current_node, []):
            if neighbor in visited:
                continue
            new_cost = current_cost + weight
            if new_cost < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                previous[neighbor] = current_node

    # Reconstruct the path
    path = []
    current = end
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return distances.get(end, float('inf')), path





def part1(maze):           # => 
    # Example usage:
    # file_path = 'maze.txt'  # The maze file
    start = (2, 0)  # Starting point S
    end = (2, 6)    # Ending point E

    adjacency_list = parse_maze(maze)
    shortest_distance, path = dijkstra(adjacency_list, start, end)

    print(f"Shortest distance: {shortest_distance}")
    print(f"Path: {path}")

def part2():            # => 
    pass

def part3():           # => 
    pass       



def solve():
    """Solve the puzzle for the given input."""
    # data, s, e = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(IN_FILE1))
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