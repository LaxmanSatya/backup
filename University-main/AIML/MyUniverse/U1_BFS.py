# What about Breath First Search

from collections import deque

def bfs_shortest_path(grid, start, target):
    """
    Finds the absolute shortest path on a 2D grid using BFS.
    
    :param grid: 2D list where 0 is walkable space and 1 is a wall/obstacle.
    :param start: Tuple (row, col) for the starting position.
    :param target: Tuple (row, col) for the destination position.
    :return: List of coordinates from start to target, or None if blocked.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Boundary check and obstacle check for start/target points
    if not (0 <= start[0] < rows and 0 <= start[1] < cols) or \
       not (0 <= target[0] < rows and 0 <= target[1] < cols) or \
       grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
        return None
        
    # Initialize the queue with the starting position
    queue = deque([start])
    
    # Keep track of visited cells to prevent infinite loops
    visited = {start}
    
    # Map to track how we reached each cell: parent_map[child] = parent
    parent_map = {start: None}
    
    # Define orthogonal movement vectors: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while queue:
        curr_row, curr_col = queue.popleft()
        
        # Target found! Reconstruct the path backwards
        if (curr_row, curr_col) == target:
            path = []
            curr = target
            while curr is not None:
                path.append(curr)
                curr = parent_map[curr]
            return path[::-1]  # Reverse to get Start -> Target order
            
        # Explore the 4 neighboring cells
        for dr, dc in directions:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            # Check grid boundaries, obstacles, and visited history
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                grid[next_row][next_col] == 0 and 
                (next_row, next_col) not in visited):
                
                queue.append((next_row, next_col))
                visited.add((next_row, next_col))
                parent_map[(next_row, next_col)] = (curr_row, curr_col)
                
    return None  # Return None if the target is unreachable

# Example Execution
if __name__ == "__main__":
    # 0 = Walkable path, 1 = Solid Wall
    maze = [,
 ,
 ,
 ,
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)  # Top-left corner
    end_pos = (4, 4)    # Bottom-right corner
    
    path = bfs_shortest_path(maze, start_pos, end_pos)
    print("Shortest Path:", path)

