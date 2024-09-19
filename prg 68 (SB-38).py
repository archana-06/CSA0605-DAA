import heapq

def dijkstra(n, edges, source, target):
    adj_list = [[] for _ in range(n)]
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))  
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if u == target:
            return current_dist
        if current_dist > dist[u]:
            continue
        for v, weight in adj_list[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    return float('inf')

n = 6
edges = [
    (0, 1, 7), (0, 2, 9), (0, 5, 14),
    (1, 2, 10), (1, 3, 15),
    (2, 3, 11), (2, 5, 2),
    (3, 4, 6), (4, 5, 9)
]
source = 0
target = 4
print(dijkstra(n, edges, source, target))  
