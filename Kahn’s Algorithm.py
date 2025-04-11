from collections import deque

def find_topological_ordering(graph):
    num_nodes = max(graph.keys()) + 1
    in_degree = [0] * num_nodes

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != num_nodes:
        return None
    return order


graph = {
    0: [1, 2, 5],
    1: [3, 2],
    2: [3, 4],
    3: [4],
    5: [4]
}

ordering = find_topological_ordering(graph)
print("Topological Order:", ordering)
