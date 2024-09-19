# Vertex Cover Approximation Algorithm

def vertex_cover(n, m, edges):
    covered_edges = set()
    vertex_cover_set = set()
    
    while len(covered_edges) < m:
        for u, v in edges:
            if (u, v) not in covered_edges:
                vertex_cover_set.add(u)
                vertex_cover_set.add(v)
                covered_edges.add((u, v))
                covered_edges.add((v, u))
                break
                
    return list(vertex_cover_set)

n = 5
m = 6
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
result = vertex_cover(n, m, edges)
print("Vertex Cover:", result)
