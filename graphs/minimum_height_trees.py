# https://leetcode.com/problems/minimum-height-trees/
from collections import defaultdict

n = 4
edges = [[1, 0], [1, 2], [1, 3]]


def bfs(src, children, graph, h, visited):
    hts = []
    if src in visited:
        return h
    visited.add(src)
    for c in children:
        hts.append(bfs(c, graph[c], graph, h + 1, visited))
    return max(hts)


def find_min_height_tree(edges):
    height_root = defaultdict(list)
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    for u, v in graph.items():
        visited = set()
        h = bfs(u, v, graph, 0, visited)
        height_root[h].append(u)
    print(height_root)
    print(height_root[min(height_root)])

print(find_min_height_tree(edges))
print(find_min_height_tree(edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))
