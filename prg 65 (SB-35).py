import heapq

def k_closest_points(points, k):
    def squared_distance(point):
        return point[0] ** 2 + point[1] ** 2

    max_heap = []
    for point in points:
        dist = squared_distance(point)
        heapq.heappush(max_heap, (-dist, point))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    return [point for (_, point) in max_heap]

points1 = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k1 = 2
print(k_closest_points(points1, k1)) 
