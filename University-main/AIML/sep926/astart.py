# [TARGET AIM] ::: Implementing A* algorithm for pathfinding in a grid-based environment.

import heapq

from asyncio import graph

def a_start(graph, heuristic, start, goal):
    # Priority queue: (f, g, node)
    open_list = []

    # Start node
    g_cost = {start : 0}
    parent = {start : None}

    f_start = g_cost[start] + heuristic[start]
    heapq.heappush(open_list, (f_start, g_cost[start], start))

    closed = set()

    while open_list:
        # select node with lowest f(n)  
        f_current, current_g, current = heapq.heappop(open_list)

        # Ignore outdateded entries
        if current_g != g_cost[current]:
            continue

        print(f'Expanding: {current} | g = {current_g},'
              f"h={heuristic[current]}, f={f_current}")

        # Goal reached
        if current == goal:
            path =[]
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path[::-1] # Return reversed path
        
        closed.add(current)

        # Expolore neighbors
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            # Found a better path
            if neighbor not in g_cost or new_g:
                parent[neighbor] = current

                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

    return None, float("inf")

# --------------------------------------------------------------------------------------------------------
#  Graph
# ---------------------------------------------------------------------------------------------------------

graph = {
    'S' : [('A', 1), ('B', 4)],
    'A' : [('S', 1), ('C', 2), ('D', 4)],
    'B' : [('S', 4), ('D', 1),],
    'C' : [('A', 2), ('B', 1), ('G', 1)],
    'G' : [('C', 5), ('D', 1)]
}

# ------------------------------------------------------------------------------------------------------------
# Heuristic values
# ------------------------------------------------------------------------------------------------------------

heuristic = {
    'S' : 6,
    'A' : 2,   
}
