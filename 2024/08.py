# Everbody Codes: 8
import os
import time

DATA1 = 4098185
DATA2 = 992

def part1(input):           # => 9879560
    # Square numbers until answer (x) is greater than input
    # x - input = missing blocks (mb)
    # x - previous square = width of base (width)
    # mb * width = solution

    prev, cur = 0,0
    for x in range(1,100000):
        cur = x**2
        if cur > input:
            break
        else:
            prev = cur
    
    missing_blocks = cur - input
    width = cur - prev

    solution = missing_blocks * width
    return solution



def part2(input):            # => 20240000
    priests = 1111
    available_blocks = 20240000
    total_blocks = 1
    # cur_width = layer * 2 - 1
    thickness = 1
    layer = 2

    while total_blocks < available_blocks:
        new_thickness = (thickness * input) % priests
        new_width = (layer * 2) - 1
        total_blocks += (new_width * new_thickness)

        layer += 1
        thickness = new_thickness
    
    blocks_needed = total_blocks - available_blocks
    solution = blocks_needed * new_width
    return solution
        




def part3(nails):       # => 
    pass


def solve():
    """Solve the puzzle for the given input."""
    start_time = time.time()
    p1 = str(part1(DATA1))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part2(DATA2))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    # start_time = time.time()
    # p3 = str(part3(data))
    # exec_time = time.time() - start_time
    # print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()