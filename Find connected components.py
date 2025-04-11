def find_connected_components(matrix):
    n = len(matrix)
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor, component)

    for i in range(n):
        if i not in visited:
            component = []
            dfs(i, component)
            components.append(component)

    return components

adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

components = find_connected_components(adj_matrix)
print(components)
