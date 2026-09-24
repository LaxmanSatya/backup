from collections import defaultdict
from typing import Self

class Graph:
    # Construct graph
    def __init__(self: Self) -> None:
        # To store graph in a Default Dictionary
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self: Self, u: int, v: int) -> None:
        self.graph[u].append(v)

    # A helper function used by DFS
    def _dfs_util(self: Self, v: int, visited: set) -> None:
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    # Main DFS function to handle both connected and disconnected graphs
    def dfs(self: Self, start_vertex: int | None = None) -> None:
        visited = set()

        # If a starting vertex is provided, run DFS from there first
        if start_vertex is not None:
            print(f"DFS starting from vertex {start_vertex}:")
            self._dfs_util(start_vertex, visited)
            print() # For newline

        # Handle remaining unvisited nodes (if the graph is disconnected)
        remaining_vertices = [v for v in self.graph if v not in visited]
        if remaining_vertices:
            print("DFS for remaining disconnected components:")
            for vertex in remaining_vertices:
                if vertex not in visited:
                    self._dfs_util(vertex, visited)
            print()


# --- Example Usage ---
if __name__ == "__main__":
    g = Graph()
    
    # Component 1 (Connected)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    # Component 2 (Disconnected from the first component)
    g.addEdge(4, 5)

    # Execute DFS starting from vertex 2
    g.dfs(start_vertex=2)
        