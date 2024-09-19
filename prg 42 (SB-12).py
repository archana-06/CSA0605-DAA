import heapq

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    min_heap = [(0, k)] 
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(min_heap, (distance, v))
    max_dist = max(dist[1:])  
    return max_dist if max_dist < float('inf') else -1

# Example usage
print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)) 
print(networkDelayTime([[1, 2, 1]], 2, 1))  
print(networkDelayTime([[1, 2, 1]], 2, 2))  
