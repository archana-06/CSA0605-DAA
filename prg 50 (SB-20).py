import numpy as np

def floyd_warshall(n, edges):
    dist = np.full((n, n), np.inf)
    np.fill_diagonal(dist, 0)
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    print_matrix(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print_matrix(dist)
    return dist

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{x if x < np.inf else "∞":>7}' for x in row))

def shortest_path(dist, start, end):
    if dist[start][end] == np.inf:
        return "No path"
    return dist[start][end]

n1 = 5
edges1 = [
    [0, 1, 2],
    [0, 4, 8],
    [1, 2, 3],
    [1, 4, 2],
    [2, 3, 1],
    [3, 4, 1]
]
dist1 = floyd_warshall(n1, edges1)

def find_city_with_max_neighbors(dist, threshold):
    max_neighbors = -1
    city_with_max_neighbors = -1
    for i in range(len(dist)):
        neighbors_count = sum(1 for j in range(len(dist)) if dist[i][j] <= threshold and i != j)
        if neighbors_count > max_neighbors:
            max_neighbors = neighbors_count
            city_with_max_neighbors = i
    return city_with_max_neighbors

threshold = 2
city = find_city_with_max_neighbors(dist1, threshold)
print(f"The city with the maximum number of neighboring cities within distance threshold {threshold} is City {city}")

n2 = 4
edges2 = [
    [1, 0, 2],
    [0, 2, 3],
    [2, 3, 1],
    [3, 0, 6],
    [2, 1, 7]
]
dist2 = floyd_warshall(n2, edges2)
print(f"Shortest path from City 2 to City 0 = {shortest_path(dist2, 2, 0)}")
