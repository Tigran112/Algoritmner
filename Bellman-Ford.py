def bellman_ford(vertices, edges, source):
    dist = {vertex: float('inf') for vertex in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Գրաֆը պարունակում է բացասական ցիկլ")
            return None

    return dist

edges = [
    ('A', 'B', 3),
    ('A', 'C', 6),
    ('B', 'D', 1),
    ('D', 'C', 1),
    ('D', 'E', 3),
    ('E', 'F', 4),
    ('F', 'C', 8),
    ('C', 'E', -2)
]

vertices = set()
for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])

source = 'A'
distances = bellman_ford(vertices, edges, source)

if distances:
    print(f"{source} Սկզբնակետից մինչև՝ ")
    for vertex, distance in distances.items():
        print(f"{vertex}\t\t{distance}")
