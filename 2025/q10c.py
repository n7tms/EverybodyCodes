import numpy as np
import more_itertools
import functools

import os


# IN_FILE2 = os.path.join("2025","inputs","2025-10.sample.txt")
# IN_FILE1 = os.path.join("2025","inputs","2025-10-1.txt")
# IN_FILE2 = os.path.join("2025","inputs","2025-10-2.txt")
IN_FILE3 = os.path.join("2025","inputs","2025-10-3.txt")

with open(IN_FILE3) as f:
    grid = np.array([[char for char in line] for line in f.read().splitlines()])

numrows,numcols = grid.shape
dragon = tuple(more_itertools.one(np.argwhere(grid=='D')))
sheep = frozenset(tuple(map(tuple, np.argwhere(grid=='S'))))
hiding = frozenset(tuple(map(tuple, np.argwhere(grid=='#'))))

@functools.cache
def num_ways(dragon,sheep,curr_move):
    if not sheep:
        return 1
    if any(x>=numrows for x,_ in sheep):
        return 0
    if curr_move == 'S':
        can_move = [(x,y) for x,y in sheep if (x+1,y)!=dragon or (x+1,y) in hiding]
        if can_move:
            answer = 0
            for x,y in can_move:
                new_sheep = frozenset({item for item in sheep if item!=(x,y)}|{(x+1,y)})
                answer += num_ways(dragon,new_sheep,'D')
            return answer
        else:
            return num_ways(dragon,sheep,'D')
    elif curr_move == 'D':
        x,y = dragon
        answer = 0
        for dx,dy in [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]:
            newx,newy = x+dx,y+dy
            if newx in range(numrows) and newy in range(numcols):
                if (newx,newy) in sheep and (newx,newy) not in hiding:
                    answer += num_ways((newx,newy),frozenset(sheep-{(newx,newy)}),'S')
                else:
                    answer += num_ways((newx,newy),sheep,'S')
        return answer

answer = num_ways(dragon,sheep,'S')
print(answer)