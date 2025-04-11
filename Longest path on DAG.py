def dfs(at, visited, ordering, graph, i):
    visited[at] = True
    for edge in graph.get(at, []):
        if not visited[edge[0]]:
            i = dfs(edge[0], visited, ordering, graph, i)
    ordering[i] = at
    return i - 1


def dag_longest_path(graph, start, num_nodes):
    ordering = [0] * num_nodes
    visited = [False] * num_nodes
    i = num_nodes - 1
    for at in range(num_nodes):
        if not visited[at]:
            i = dfs(at, visited, ordering, graph, i)

    dist = [float('-inf')] * num_nodes
    dist[start] = 0
    for node_index in ordering:
        if dist[node_index] != float('-inf'):
            for edge in graph.get(node_index, []):
                new_dist = dist[node_index] + edge[1]
                if new_dist > dist[edge[0]]:
                    dist[edge[0]] = new_dist
    return dist


graph = {
    0: [(1, 3), (2, 2), (5, 3)],
    1: [(3, 1), (2, 6)],
    2: [(3, 1), (4, 10)],
    3: [(4, 5)],
    5: [(4, 7)]
}
num_nodes = 7

distances = dag_longest_path(graph, 0, num_nodes)
print("Longest Path Distances from Node 0:", distances)
