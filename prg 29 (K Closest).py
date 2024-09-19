"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).The distance between two points on the X-Y plane is the Euclidean
distance (i.e., √(x1 - x2)2 + (y1 - y2)2). You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).
"""
import heapq

def kClosest(points, k):
    max_heap = []
    for (x, y) in points:
        distance = -(x**2 + y**2)  
        heapq.heappush(max_heap, (distance, (x, y)))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [point for (_, point) in max_heap]
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(kClosest(points, k))










