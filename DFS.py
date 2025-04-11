def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

graph = {0: [7, 9, 11],
         1: [],
         2: [12],
         3: [2, 4],
         4: [],
         5: [],
         6: [5],
         7: [6, 3, 11],
         8: [1, 12],
         9: [8, 10, 0],
         10: [1],
         11: [],
         12: [2]
         }

first_node = int(input("enter the first node: "))
dfs_recursive(graph, first_node)