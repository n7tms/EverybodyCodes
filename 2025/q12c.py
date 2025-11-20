# Finds connected components, then merges components upwards sorted from smallest to largest value
# Keeps track of local maxima while merging, then finds the 3 best locations to shoot barrels
# Runs in ~100 ms on my input (excluding file i/o and parsing)

import time
import os

IN_FILE3 = os.path.join("2025","inputs","2025-12-3.txt")

# 4-connected directions, starting at east and going clockwise
DIRS_4 = [
    (0, 1),  # East
    (1, 0),  # South
    (0, -1), # West
    (-1, 0), # North
]

# Disjoint set union
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        
        parent = self.find(self.parents[x])
        self.parents[x] = parent
        return parent

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: # Already in same set
            return
        
        # Smaller size attaches to larger size
        if self.sizes[a] <= self.sizes[b]:
            self.parents[a] = b
            self.sizes[b] += self.sizes[a]
        else:
            self.parents[b] = a
            self.sizes[a] += self.sizes[b]


# Parse input
with open(IN_FILE3) as f:
    grid = [list(map(int, list(row))) for row in f.read().splitlines()]
h, w = len(grid), len(grid[0])

start_time = time.perf_counter_ns()


# Build connected components
cc_dsu = DSU(w * h)

def to_id(r, c):
    return r*w + c

# Union down and to the right
for r in range(h):
    for c in range(w):
        # Down
        if (r+1 < h) and (grid[r][c] == grid[r+1][c]):
            cc_dsu.union(to_id(r,c), to_id(r+1,c))
        # Right
        if (c+1 < w) and (grid[r][c] == grid[r][c+1]):
            cc_dsu.union(to_id(r,c), to_id(r,c+1))

# Track each cell's region, along with each region's size and the unique cells per region
cc = [[0]*w for _ in range(h)]
group_sizes = dict()
nums_present = [list() for _ in range(10)]
for r in range(h):
    for c in range(w):
        parent = cc_dsu.find(to_id(r, c))
        cc[r][c] = parent
        if parent not in group_sizes:
            nums_present[grid[r][c]].append((r,c))
        group_sizes[parent] = cc_dsu.sizes[parent]


# Make graph
seen = [[False]*w for _ in range(h)]

def get_neighbors(start_pos):
    # Do flood fill in contiguous region plus barrels on the edge
    neighbors = set()
    stack = [start_pos]
    seen[start_pos[0]][start_pos[1]] = True
    
    start_region = cc[start_pos[0]][start_pos[1]]
    start_value = grid[start_pos[0]][start_pos[1]]
    
    while stack:
        r, c = stack.pop()
        for dr, dc in DIRS_4:
            new_r, new_c = (r+dr, c+dc)
            if (0 <= new_r < h) and (0 <= new_c < w) and (not seen[new_r][new_c]):
                # Add to flood fill in same region
                if cc[new_r][new_c] == start_region:
                    stack.append((new_r, new_c))
                    seen[new_r][new_c] = True
                # Add to neighbors
                elif grid[new_r][new_c] > start_value:
                    neighbors.add(cc[new_r][new_c])
    
    return neighbors

# Merge regions upwards, from lowest values to highest values
children = {x: set([x]) for x in group_sizes.keys()}
local_maxima = []
for cells in nums_present:
    for r, c in cells:
        neighbors = get_neighbors((r, c))
        region_val = cc[r][c]
        if neighbors:
            for neighbor in neighbors:
                children[neighbor] |= children[region_val]
        else:
            local_maxima.append(region_val)

# Get best fireball locations
total = 0
burned_regions = set()
for _ in range(3):
    best = 0
    best_seen = None
    for region in local_maxima:
        exploded = sum(group_sizes[child] for child in children[region] if child not in burned_regions)
        if exploded > best:
            best = exploded
            best_seen = children[region]
    
    total += best
    burned_regions |= best_seen

end_time = time.perf_counter_ns()

print(f'Time: {(end_time-start_time)/10**6:.1f} ms')
print(total)
