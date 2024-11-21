# Everybody Codes: 13

import os
import time
import heapq


# IN_FILE1 = os.path.join("2024","inputs","2024-13-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-13-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-13-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-13-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-13-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-13-3.txt")


def parse_maze_to_dict(file_path):
    with open(file_path, 'r') as f:
        maze = [line.strip() for line in f.readlines()]

    rows, cols = len(maze), len(maze[0])
    maze_dict = {}
    start_node = ()
    end_node = ()

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                if maze[r][c] == 'S':
                    start_node = (r,c) 
                if maze[r][c] == 'E':
                    end_node = (r,c) 
                
                # Cost to enter the current cell
                cell_cost = int(maze[r][c]) if maze[r][c].isdigit() else 0
                neighbors = {}
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                        neighbors[(nr, nc)] = int(maze[nr][nc]) if maze[nr][nc].isdigit() else 0
                maze_dict[(r, c)] = [cell_cost, neighbors]

    return maze_dict, start_node, end_node

def parse_maze_to_dict3(file_path):
    # A slightly different parse routine for part 3.
    with open(file_path, 'r') as f:
        maze = [line.strip() for line in f.readlines()]

    rows, cols = len(maze), len(maze[0])
    maze_dict = {}
    start_nodes = []
    end_node = ()

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                # this if block is the only change in this code, to generate a [] of start nodes
                if maze[r][c] == 'S':
                    start_nodes.append((r,c))
                if maze[r][c] == 'E':
                    end_node = (r,c) 
                
                # Cost to enter the current cell
                cell_cost = int(maze[r][c]) if maze[r][c].isdigit() else 0
                neighbors = {}
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                        neighbors[(nr, nc)] = int(maze[nr][nc]) if maze[nr][nc].isdigit() else 0
                maze_dict[(r, c)] = [cell_cost, neighbors]

    return maze_dict, start_nodes, end_node


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
                # determine if its shorter to go up the lift or down the lift
                nc = abs(cell_cost - move_cost)
                if nc > 5:
                    new_cost = current_cost + (10 - nc) + 1
                else:
                    new_cost = current_cost + nc + 1



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




def part1(maze):           # => 145
    adjacency_list, start, end = parse_maze_to_dict(maze)
    shortest_distance, path = dijkstra_with_dict(adjacency_list, start, end)

    return shortest_distance


def part2(maze):            # => 610
    adjacency_list, start, end = parse_maze_to_dict(maze)
    shortest_distance, path = dijkstra_with_dict(adjacency_list, start, end)

    return shortest_distance


def part3(maze):           # => 532
    # There are multiple starting points.
    # Use a slightly different parser that returns a "list" of start nodes.
    adjacency_list, starts, end = parse_maze_to_dict3(maze)

    # find the distance from every start to the end
    distances = []
    for s in starts:
        shortest_distance, path = dijkstra_with_dict(adjacency_list, s, end)
        distances.append(shortest_distance)

    # return the shortest distance
    return min(distances)


def solve():
    """Solve the puzzle for the given input."""
    start_time = time.time()
    p1 = str(part1(IN_FILE1))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(IN_FILE2))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    start_time = time.time()
    p3 = str(part3(IN_FILE3))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()