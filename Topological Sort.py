def dfs(graph, vertex, stack, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, stack, visited)
    stack.append(vertex)

def topological_sort(graph):
    stack = []
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, stack, visited)
    ordering = []
    while stack:
        ordering.append(stack.pop())
    return ordering
graph = {
    "C": ["A","B"],
    "A": ["D"],
    "B": ["D"],
    "D": ["H","G"],
    "E": ["D", "F"],
    "F": ["K","J"],
    "K": ["J"],
    "J": ["M","L"],
    "G": ["I"],
    "H": ["J","I"],
    "I": ["L"],
    "M":[],
    "L":[]
}

print(topological_sort(graph))
