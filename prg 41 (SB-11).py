def findTheCity(n, edges, distanceThreshold):
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    min_city_count = float('inf')
    result_city = -1
    
    for i in range(n):
        count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
        if count <= min_city_count:
            min_city_count = count
            result_city = i
    
    return result_city
print(findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))  
