import numpy as np
import more_itertools
import heapq
from collections import defaultdict
import math
import os


# IN_FILE2 = os.path.join("2025","inputs","2025-10.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs","2025-10-1.txt")
IN_FILE2 = os.path.join("2025","inputs","2025-10-2.txt")
# IN_FILE3 = os.path.join("2025","inputs","2025-10-3.txt")

with open(IN_FILE2) as f:
    grid = np.array([[char for char in line] for line in f.read().splitlines()])

numrows,numcols = grid.shape
start = tuple(more_itertools.one(np.argwhere(grid=='D')))
sheep = np.argwhere(grid=='S')
sheep = tuple(map(tuple, sheep))
hiding = np.argwhere(grid=='#')
hiding = tuple(map(tuple, hiding))

num_rounds = 20

def dijkstra_function(start,distance_function,max_distance):
    visited = {}
    queue = [(0,start)]
    time_dict = defaultdict(lambda: math.inf, {start:0})
    while queue:
        time,loc = heapq.heappop(queue)
        if time >= max_distance:
            break
        if loc in visited:
            continue
        visited[loc] = True
        neighbours = distance_function(loc)
        for coord,distance in neighbours:
            newtime = time+distance
            if coord not in visited:
                if newtime < time_dict[coord]:
                    time_dict[coord] = newtime
                    heapq.heappush(queue,(newtime,coord))
    time_dict = {key:value for key,value in time_dict.items() if value<=max_distance}
    return time_dict

def distance_function(coords):
    x,y = coords
    output = []
    for dx,dy in [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]:
        newx,newy = x+dx,y+dy
        if newx in range(numrows) and newy in range(numcols):
            output.append([(newx,newy),1])
    return output
            
endings = dijkstra_function(start,distance_function,num_rounds)

def sheep_walk(sheep_start):
    output = {}
    x,y = sheep_start
    for time in range(num_rounds+1):
        newx,newy = x+time,y
        if newx in range(numrows) and (newx,newy) not in hiding:
            output[(newx,newy)] = [time,time+1] if time<num_rounds else [time]
    return output

def is_sheep_caught(sheep_start,endings):
    sheep_locations = sheep_walk(sheep_start)
    for location in sheep_locations:
        if location in endings:
            if any(endings[location] <= item and endings[location]%2==item%2 for item in sheep_locations[location]):
                return True
    return False

answer = sum(is_sheep_caught(sheep_start,endings) for sheep_start in sheep)
print(answer)