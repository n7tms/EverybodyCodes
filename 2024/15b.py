## Attribution:
## i_have_no_biscuits (reddit)
## https://topaz.github.io/paste/#XQAAAQCMDgAAAAAAAAARiAcH4cNcktpwLwcwtIOgpuFZqTzxZgRurfBoL6pYx4GY93Y0ok5Atwf3VpZxrrpdFHTE8QqSjpN9g46IES8e/S1MmP/gIb1bTFYSmc51HogGmZKgTiqlpqU+v3c+gSTr+loSqfbla4T3dEYfNGXtZy/250rP+bMFBkVHtC4IUgRe8MoltJLy+FMHXtMwlXwiE73H8rdGvWef6RSwOqlpcw0ELyPapyCqDuJb0hvab9ZytuP7vZzICWQB1ogH//+Sh0xusAdbF8Lm2SNEyUwDMm+49EFT6h+ajYHOmCWyPqPvm4qoL7jZ3jM/Mypu89fGNoysXqUSegYFXtaFFhXUIYzzTRO+Hpj2UennClJnybhzxWr3bPpeg+O6PtCKZLGXbOrS0BsTBTG7QBtIk3NivgYSLVu4STWeJzS6oO2+qfQH3jN/yQVWpT5U1xFNEEr/RUlqUK0y7X3bC3FqC41NTbeaecHTvt9ROIlTK9PA4vQ08aCjr0gvDgecHHoAunmK7jfsXsEm+TK1amMYhDljOax/DcER5HsHSvZuqXlZ/r2XVarMDWWe7NxcVnyHflIoUY2QgeZqafTM5A1HP0A/AsFdnFHjMuR0HXirWp77MESzx1rzcthtlq0ii5vgcxKzrUWGzuIVfH/8dpLEsicqZiDrLZVE0AevKlr2qKzraVahDBp6f+d095+9fE5rgrs1AloEsbc5yjFyVFQhmOUn2teWRJLXA6IFbIYC3xIbNB6Pq3AbbvZoqwIe/1/CNZfnn0lESsAXs8J9K8bMsd8+fUqSe5K61lKuTPc4xK122sj4htBfN0NBAgN69PoMKZWyeUmk7TEOLsGTXcn6eAGZnBXSE2Hg9IxoDAKa97AWRz7pXVKrxctKshOTDZzjGttqP5qypaIP0wHWfBfj3/eeizBDQIAFA53wyZOon7j5+cBDguDPN+TENqDn1/MDXbKvcWJltxYPTiMMayrJuzsL1mNOUAVe3CLVJ3toZOsaBl3/SJI9DZAfchUFD1Uey2kOMehxmrkdkhfI9TSORIMTWaF8B1d/Dup8QIOhBVNmxDffjSP4omGwFLgQ46Yx+spYcQCsUOEOCOP25Uys7zywb0ll47NV8agIkHWfzPZO7AJj2lZ3tiZogoytBu+UxB6nh1wo9r2JXD2BgjwRvyO1Jo4rQntjLamHs+gKxdh2r9ZpkOTuD4j8SVsCaH+F6Qcgb4/f+WL4BizemwOuBqBpl25Ovz4h4trb+a7ajYp+5jTsj0yUzq6mBUx2h7nXGxr22sqwRfGvV+YgSPCcHTcEP3/dBejSEjYl5Wm0bmk3LsOnTqE72FxDsuJMg8TQd7+vJNzdipste1kxVAK2DlYzuQVlW8YUQHUgw0gA+keT+R3DZSZ8akjaeHUENYQzxmGDSW9SepfRX0Lqr12/B+BMCbVZFARXCFq8Ih6xCCE+1CaN5a343wy1FxQD3kTXx9Lvzgf1iD7Brqha7w607I3bdtPFk4ToJVQrwNOtzZJt4EAKRxupnAe+bTE5OZd5wNP2EeM7LSb3V8v52LaSPbvKasU39WUke61+k4voSj//rP8MMe5Ipl9UhbW+LDcLiQ4Kr4Y99cFaI0+oyiWHI8F4k6vpzJueM4u1sZunaMXJCve+aKxmMz474bmFTorgb7X9l4i1HMS+DRF/FrpsYNjBIE5cWoS2hs/DAAhDNkEXwjt3s5CoADtdbrrcQwSfEFKOPdAbIwEwB35XD+wJly6LhfWUvQzxidd1Kqueo2Bv8ipTDY4+9XSHlOSSjhz7KyYxoime5jWABfD4TSRY1Tl868E9I0Ubq+W1Nm4/Y4aQT1ecDTRFpJv0c413HVBzgDCRKlDMTTDI602SwiA/f8IpFg9edagyAOa0SrJV7/m8GoWLFHHLRwRyVHpS3sOu+67x7WBeFzC8kP6wr98iaGRHwhDQnbV0Xq3T/7WbSb0=


# This parses the data into a dictionary of allowed places to walk, and another dictionary of Points of Interest.
# The 'Start' POI is the only free path on the first row (if it exists!)
from collections import defaultdict
import os

IN_FILE1 = os.path.join("2024","inputs","2024-15-1.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-15-2.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-15-3.txt")


def parse_maze_to_dict(file_path):
    with open(file_path, 'r') as f:
        maze = [line.strip() for line in f.readlines()]
    return maze

def parse(data):
    path, poi = dict(), defaultdict(set)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in '#~': continue
            path[y,x] = c
            if y == 0 and c == '.':
                poi["Start"].add((y,x))
                path[y,x] = "Start"
            if c != '.':
                poi[c].add((y,x))
    return poi, path


# Find the distances from src to all the Points of Interest
def find_distances(path, src, poi):
    distances = {}
    boundary, seen, dist = set([src]), set(), 0
    while boundary:
        newboundary = set()
        for y, x in boundary:
            if (y, x) in path and path[y,x] in poi:
                distances[(path[y,x], (y,x))] = dist                
            seen.add((y, x))
            for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny, nx = y+dy, x+dx
                if (ny,nx) not in seen and (ny,nx) in path:
                    newboundary.add((ny,nx))
        dist += 1
        boundary = newboundary
    return distances


# Finds the minimum cost of following a specified route
def follow_route(route, distances):
    cur = {(c, loc):0 for (c, loc) in distances if c==route[0]}
    for target in route[1:]:
        dests = {(c, loc):10**9 for (c, loc) in distances if c==target}
        for src in cur:
            for dest in dests:
                dests[dest] = min(dests[dest], cur[src]+distances[src][dest])  
        cur = dests      
    return min(cur.values())


# Tries all the possible permutations of picking up items, starting and ending at a specified POI.
from itertools import permutations
def find_best_route(data, start="Start", split=None, choose=None):
    poi, path = parse(data)

    # We may have to split a POI into individual points that all need visiting.
    if split:
        locs = poi.pop(split)
        for i, loc in enumerate(locs):
            poi[split+str(i)] = set([loc])
            path[loc] = split+str(i)

    # We may have to choose just one of the start points based on a choice function.
    if choose:
        locs = poi.pop(start)
        for loc in locs:
            path[loc] = "."
        choice = choose(locs)
        poi[start] = set([choice])
        path[choice] = start

    distances = {}
    for c in poi:
        for loc in poi[c]:
            distances[(c, loc)] = find_distances(path, loc, poi)

    targets = set(poi) - {start}
    best_dist = 10**9
    for route in permutations(targets):
        route = [start] + list(route) + [start]
        dist = follow_route(route, distances)
        best_dist = min(best_dist, dist)
    return best_dist


def main():
    data1 = parse_maze_to_dict(IN_FILE1)  # 208
    print("Part 1:", find_best_route(data1))
    data2 = parse_maze_to_dict(IN_FILE2)    # 524
    print("Part 2:", find_best_route(data2))

    # Part 3 is too big to do naively (15! is in the trillions!)
    # It's formed of 3 columns which we can solve separately, and then add the scores together (+12 for the connection)

    data = parse_maze_to_dict(IN_FILE3)

    col_width = len(data[0])//3
    left = [line[:col_width] for line in data]
    middle = [line[col_width:2*col_width] for line in data]
    right = [line[2*col_width:] for line in data]

    l = find_best_route(left, 'E', choose=max)        # left route starts & ends at E
    m = find_best_route(middle, "Start", split="K")   # middle route has to go through both K's
    r = find_best_route(right, 'R', choose=min)       # end route starts & ends at R

    print("Part 3:", l+m+r+6*2)

    
if __name__ == "__main__":
    main()
