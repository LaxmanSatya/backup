'''
using BFS< simulate shortest route identification in a hospital emergency evacuation system. Given a 2d grid representing a hosptial floor plan(with walls, rooms, and exit points), find the shortest evacuation path from any patient room to the nearest emergency exit write source code in python and output also


A Breadth-First Search (BFS) algorithm guarantees the shortest path in an unweighted 2D grid. In this simulation, the hospital grid uses:

'P': Patient room (start)

'E': Emergency exit (target)

'#': Wall / obstacle (cannot pass)

'.': Open corridor / clear pathway

'*': Path taken during evacuation

'''

from collections import deque


def find_evacuation_route(grid, start_pos):
    rows = len(grid)
    cols = len(grid[0])
    start_r, start_c = start_pos

    # Queue stores: (row, col)
    queue = deque([(start_r, start_c)])

    # Track visited cells and their predecessors for path reconstruction
    # parent[(r, c)] = (prev_r, prev_c)
    visited = {(start_r, start_c)}
    parent = {(start_r, start_c): None}

    # 4-directional movement: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    exit_pos = None

    while queue:
        r, c = queue.popleft()

        # Check if an emergency exit is reached
        if grid[r][c] == "E":
            exit_pos = (r, c)
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Boundary and obstacle checks
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != "#" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    if not exit_pos:
        return None, float("inf")

    # Reconstruct path from exit back to patient room
    path = []
    curr = exit_pos
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path, len(path) - 1


def display_evacuation_map(grid, path):
    display_grid = [row[:] for row in grid]
    # Mark intermediate path steps
    for r, c in path[1:-1]:
        display_grid[r][c] = "*"

    print("Evacuation Floor Plan:")
    for row in display_grid:
        print("  " + " ".join(row))


# ----------------------------------------------------
# Hospital Floor Simulation Setup
# ----------------------------------------------------
# P = Patient Room, E = Emergency Exit, # = Wall, . = Corridor
hospital_grid = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", ".", ".", "#", ".", ".", ".", "E", "#"],
    ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#", ".", ".", "#"],
    ["#", "E", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

# Locate Patient Position
start = None
for i in range(len(hospital_grid)):
    for j in range(len(hospital_grid[0])):
        if hospital_grid[i][j] == "P":
            start = (i, j)
            break
    if start:
        break

path, step_count = find_evacuation_route(hospital_grid, start)

if path:
    print(f"Nearest Exit Found at: {path[-1]}")
    print(f"Total Steps / Distance: {step_count} units")
    print(f"Evacuation Coordinates: {path}\n")
    display_evacuation_map(hospital_grid, path)
else:
    print("No accessible evacuation route available.")

'''
::: ----- OUTPUT ----- :::

Nearest Exit Found at: (1, 8)
Total Steps / Distance: 9 units
Evacuation Coordinates: [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7), (1, 8)]

Evacuation Floor Plan:
  # # # # # # # # # #
  # P * * # * * * E #
  # # # * # * # # # #
  # . . * * * . . . #
  # . # # # # # . . #
  # E # . . . . . . #
  # # # # # # # # # #
'''
