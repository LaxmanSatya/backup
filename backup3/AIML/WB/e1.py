# Why Prefer BFS over DFS
'''
Because the BFS level by level explore in order from start.

first reach target.
'''
'''
# BFS
from collections import deque

def bfs_pathfinding(grid, start, end):
    rows = len(grid) # gives number of rows
    cols = len(grid[0]) # gives number of columns
    queue = deque([start])

    parent = {start : None}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    while queue:
        curr_r, curr_c = queue.popleft()'''

r'''
Implementing Graph by direct mapping connections

'''
_map = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : [],
    'D' : []
} 
        
def run_bfs(graph, start_node):
    line = [start_node] # acts like a queue

    cheaked_off = {start_node} # Visted Node List


    # BFS Starts from the Node
    print("Inilizing BFS ::: FRom NODE {}".format(start_node))

    while len(line) > 0: pass

'''
# 1. Define the Map (Graph)
# This represents: A connects to B and C; B connects to D; C and D have no new paths.
my_map = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# 2. Define the BFS Function
def run_bfs(graph, start_node):
    # 'line' acts as our Queue (Grocery Line)
    line = [start_node]
    
    # 'checked_off' acts as our Visited checklist (Set)
    checked_off = {start_node}
    
    print(f"--- Starting BFS from node {start_node} ---")
    
    # Keep looping as long as there is someone waiting in line
    while len(line) > 0:
        # Take the first node from the front of the line
        current = line.pop(0)
        print(f"Currently processing: {current}")
        
        # Look at every neighbor connected to the current node
        for neighbor in graph[current]:
            # If we haven't seen this neighbor before
            if neighbor not in checked_off:
                checked_off.add(neighbor)   # Mark as checked off
                line.append(neighbor)        # Send them to the back of the line
                print(f"  -> Found new neighbor {neighbor}! Added to back of the line.")

# 3. Run the implementation
run_bfs(my_map, 'A')

'''   

r'''
expanded_map = {
    'A': ['B', 'C', 'F'],  # Layer 0 points to all Layer 1 nodes
    'B': ['D'],            # B points to D
    'C': ['E'],            # C points to E
    'F': ['G'],            # F points to G
    'D': [],               # Dead ends
    'E': [],
    'G': []
}

       Layer 0         Layer 1         Layer 2
       
                         /——— B ———————— D
                        /
                       A ———— C ———————— E
                        \
                         \——— F ———————— G


'''

_map : dict = {
    'a' : ['b', 'c'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g'],
    'd' : [],
    'e' : [],
    'f' : [],
    'g' : []
}

