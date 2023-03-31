from collections import defaultdict


class Graph:
    visited = []

    def __init__(self):
        self.children = defaultdict(list)

    def add_edge(self, u, v):
        self.children[u].append(v)

    def bfs(self, source):
        visited = [False] * (max(self.children) + 1)
        visited[source] = True
        queue = list()
        queue.append(source)
        for v in self.children[source]:
            if visited[v] is False:
                queue.append(v)
                visited[v] = True

    def dfs(self, v):
        Graph.visited.append(v)
        for child in self.children[v]:
            if child not in Graph.visited:
                print(child)
                self.dfs(child)
