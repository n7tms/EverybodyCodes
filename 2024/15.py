# Everybody Codes: 15

import os
import time
import heapq


IN_FILE1 = os.path.join("2024","inputs","2024-15-1.sample.txt")
# IN_FILE1 = os.path.join("2024","inputs","2024-15-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-15-2.sample.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-15-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-15-3.sample.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-15-3.txt")


def parse_maze_to_dict(file_path):
    with open(file_path, 'r') as f:
        maze = [line.strip() for line in f.readlines()]

    rows, cols = len(maze), len(maze[0])
    maze_dict = {}
    start_node = ()
    herbs = []

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                if r == 0 and maze[r][c] == '.':
                    start_node = (r,c) 
                if maze[r][c] == 'H':
                    herbs.append((r,c))
                
                # Cost to enter the current cell
                cell_cost = 1
                neighbors = {}
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                        neighbors[(nr, nc)] = 1 if maze[nr][nc] == '.' else 0
                maze_dict[(r, c)] = [cell_cost, neighbors]

    return maze_dict, start_node, herbs

def dijkstra_with_dict(maze_dict, start, end):
    # Priority queue: (cost, node)
    pq = [(0, start)]
    distances = {start: 0}
    previous = {}
    visited = set()

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # Skip already visited nodes
        if current_node in visited:
            continue
        visited.add(current_node)

        # Process neighbors
        if current_node in maze_dict:
            cell_cost, neighbors = maze_dict[current_node]
            for neighbor, move_cost in neighbors.items():
                new_cost = move_cost
                if new_cost < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
                    previous[neighbor] = current_node

    # Reconstruct the shortest path if we reached the end
    if end in distances:
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        return distances[end], path

    # If the end node was never reached
    return float('inf'), []    

def part1(maze):           # => not 226
    adjacency_list, start, end = parse_maze_to_dict(maze)
    shortest_distance, path = dijkstra_with_dict(adjacency_list, start, end)

    return shortest_distance


def part2(chariots):            # => 
    pass



def part3(nails):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(data))
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