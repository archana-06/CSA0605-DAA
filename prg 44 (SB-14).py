import heapq
from collections import defaultdict

def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    for (a, b), prob in zip(edges, succProb):
        graph[a].append((b, prob))
        graph[b].append((a, prob))
    
    max_heap = [(-1.0, start)]
    visited = set()
    
    while max_heap:
        prob, node = heapq.heappop(max_heap)
        prob = -prob
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == end:
            return prob
        
        for neighbor, edge_prob in graph[node]:
            if neighbor not in visited:
                new_prob = prob * edge_prob
                heapq.heappush(max_heap, (-new_prob, neighbor))
    
    return 0.0

print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
