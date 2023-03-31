# https://leetcode.com/problems/number-of-operations-to-make-network-connected/solutions/477679/python-count-the-connected-networks/?orderBy=most_votes


def find_num_connected_networks(connections, n):
    if len(connections) < n - 1:
        return -1
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)
    visited = set()

    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        for n in graph[node]:
            dfs(n)
        return 1
    return sum(dfs(i) for i in range(n)) -1


n = 4
connections = [[0,1],[0,2],[1,2]]
print(find_num_connected_networks(connections, n))
