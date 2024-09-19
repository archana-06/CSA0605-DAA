def graph_coloring(edges, n):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    color = [-1] * n
    def is_safe(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True

    def color_graph(node):
        if node == n:
            return True
        
        for c in range(n):
            if is_safe(node, c):
                color[node] = c
                if color_graph(node + 1):
                    return True
                color[node] = -1
        
        return False

    color_graph(0)
    return len(set(color))

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
max_colored_regions = graph_coloring(edges, n)
print(max_colored_regions)
