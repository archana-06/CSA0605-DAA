import numpy as np

def floyd_warshall(n, edges):
    # Initialize distance matrix with infinity and set diagonal to 0
    dist = np.full((n, n), np.inf)
    np.fill_diagonal(dist, 0)

    # Update distance matrix based on edges
    for u, v, w in edges:
        dist[u][v] = w

    print("Distance matrix before Floyd-Warshall:")
    print_matrix(dist)

    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("Distance matrix after Floyd-Warshall:")
    print_matrix(dist)

    return dist

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{x if x < np.inf else "∞":>7}' for x in row))

def shortest_path(dist, start, end):
    if dist[start][end] == np.inf:
        return "No path"
    return dist[start][end]

# Test case 1
n1 = 4
edges1 = [
    [0, 1, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 1]
]
dist1 = floyd_warshall(n1, edges1)
print(f"City 0 to City 2 = {shortest_path(dist1, 0, 2)}")

# Test case 2
n2 = 6
edges2 = [
    [0, 1, 1],
    [0, 2, 5],
    [1, 2, 2],
    [1, 3, 1],
    [2, 4, 3],
    [3, 4, 1],
    [3, 5, 6],
    [4, 5, 2]
]
dist2 = floyd_warshall(n2, edges2)
print(f"Router 0 to Router 5 = {shortest_path(dist2, 0, 5)}")

# Simulate link failure between Router B (1) and Router D (3)
edges2.remove([1, 3, 1])
print("Distance matrix after link failure:")
dist2 = floyd_warshall(n2, edges2)
print(f"Router 0 to Router 5 = {shortest_path(dist2, 0, 5)}")
