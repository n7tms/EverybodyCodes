from collections import deque
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)





# Function to add an edge between vertices x and y
def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

# Function to print the parent of each node
def printParents(node, adj, parent):
    # current node is Root, thus, has no parent
    if parent == 0:
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node, parent))

    # Using DFS
    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)

# Function to print the children of each node
def printChildren(Root, adj):
    # Queue for the BFS
    q = deque()
    # pushing the root
    q.append(Root)
    # visit array to keep track of nodes that have been
    # visited
    vis = [0] * len(adj)
    # BFS
    while q:
        node = q.popleft()
        vis[node] = 1
        print("{}->".format(node)),
        for cur in adj[node]:
            if vis[cur] == 0:
                print(cur),
                q.append(cur)
        print()

# Function to print the leaf nodes
def printLeafNodes(Root, adj):
    # Leaf nodes have only one edge and are not the root
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != Root:
            print(i),

# Function to print the degrees of each node
def printDegrees(Root, adj):
    for i in range(1, len(adj)):
        print(i, ":"),
        # Root has no parent, thus, its degree is equal to
        # the edges it is connected to
        if i == Root:
            print(len(adj[i]))
        else:
            print(len(adj[i]) - 1)

