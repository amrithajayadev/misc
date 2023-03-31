# edges = [[0, 1], [1, 2], [2, 0]]
from collections import defaultdict

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# graph = {}


def dfs(graph, source, dest, visited):
    if source == dest:
        return True
    if source in visited:
        return False

    visited.add(source)
    for node in graph[source]:
        if dfs(graph, node, dest, visited):
            return True
    return False


# # create the graph
# for u, v in edges:
#     if u in graph:
#         graph[u].append(v)
#     else:
#         graph[u] = [v]

graph = defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = set()
if dfs(graph, 0, 2, visited):
    print("True")
else:
    print("False")