from collections import defaultdict
from typing import Self

class Graph:
    def __init__(self : Self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self : Self, u : int, v : int) -> None:
        self.graph[u].append(v)

    def _dfs_util(self : Self, v : int, visited : set) -> None:
        visited.add(v)
        print(v, end = ' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def dfs(self : Self, start_vertex : int | None = None) -> None:
        visited = set()

        if start_vertex is not None:
            print(f'DFS starting from vertex {start_vertex}:')
            self._dfs_util(start_vertex, visited)
            print()

        remaining_vertices = [v for v in self.graph if v not in visited]
        if remaining_vertices:
            print('DFS for remaining disconnected components:')
            for vertex in remaining_vertices:
                if vertex not in visited:
                    self._dfs_util(v = vertex, visited = visited)
                    
            print()

if __name__ == '__main__':
    gp = Graph()

    gp.addEdge(0, 1)
    gp.addEdge(0, 2)
    gp.addEdge(1, 2)
    gp.addEdge(2, 0)
    gp.addEdge(2, 3)
    gp.addEdge(3, 3)

    gp.addEdge(4, 5)

    gp.dfs(start_vertex = 2)
        