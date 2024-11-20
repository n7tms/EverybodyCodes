# Everybody Codes: 06

import time
from collections import defaultdict, deque
import itertools
import os


# IN_FILE1 = os.path.join("2024","inputs","2024-06-1.sample.txt")
IN_FILE1 = os.path.join("2024","inputs","2024-06-1.txt")
# IN_FILE2 = os.path.join("2024","inputs","2024-06-2.sample.txt")
IN_FILE2 = os.path.join("2024","inputs","2024-06-2.txt")
# IN_FILE3 = os.path.join("2024","inputs","2024-06-3.sample.txt")
IN_FILE3 = os.path.join("2024","inputs","2024-06-3.txt")

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_tree(file_path):
    # Parse the file and build a tree with unique fruit nodes
    tree_nodes = {}
    fruit_counter = itertools.count(1)  # Counter for unique fruit nodes
    
    with open(file_path, 'r') as file:
        for line in file:
            parent, children = line.strip().split(":")
            children = children.split(",")
            
            if parent != 'ANT' and parent != 'BUG':
                if parent not in tree_nodes:
                    tree_nodes[parent] = TreeNode(parent)
                
                for child in children:
                    if child != 'ANT' and child != 'BUG':
                        if child == "@":
                            # Create a unique fruit node
                            fruit_name = f"@{next(fruit_counter)}"
                            fruit_node = TreeNode(fruit_name)
                            tree_nodes[parent].children.append(fruit_node)
                        else:
                            if child not in tree_nodes:
                                tree_nodes[child] = TreeNode(child)
                            tree_nodes[parent].children.append(tree_nodes[child])
    
    return tree_nodes.get("RR", None)  # Root node    

def find_fruit_paths(root):
    if not root:
        return []
    
    # Traverse the tree using BFS to find all paths to fruits
    paths_to_fruits = []
    queue = deque([(root, [root.name], 0)])  # (current node, path, distance)
    
    while queue:
        current_node, path, distance = queue.popleft()
        
        # Check if the node is a fruit node
        if current_node.name.startswith("@"):
            paths_to_fruits.append((path, distance))
        else:
            for child in current_node.children:
                queue.append((child, path + [child.name], distance + 1))
    
    return paths_to_fruits



def part1(infile, onlyfirsts):           # => RRVKKPGTLZTX@
    root = build_tree(infile)
    paths_to_fruits = find_fruit_paths(root)

    # print("Paths to fruits and their distances:")
    # Find the path that is unique
    p2f = {}
    for path, distance in paths_to_fruits:
        if distance in p2f:
            p2f[distance].append(path)
        else:
            p2f[distance] = [path]

    p2f2 = ''
    for k,v in p2f.items():
        if len(v) == 1:
            if onlyfirsts:
                for i in v[0]:
                    p2f2 = p2f2 + i[0]
            else:
                p2f2 = ''.join(v[0])
        
    return p2f2
    

def part2(clappers):            # => RLFKHKDZRC@
    pass       



def part3(clappers):       # => RCDSHBSVDPRG@
    pass       



def solve():
    """Solve the puzzle for the given input."""
    # data = parse(IN_FILE1)
    start_time = time.time()
    p1 = str(part1(IN_FILE1, False))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE2)
    start_time = time.time()
    p2 = str(part1(IN_FILE2, True))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")

    # data = parse(IN_FILE3)
    start_time = time.time()
    p3 = str(part1(IN_FILE3, True))
    exec_time = time.time() - start_time
    print(f"part 3: {p3} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()