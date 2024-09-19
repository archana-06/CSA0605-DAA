class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph.sort()
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            w, u, v = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        return result

def is_mst_unique(n, m, edges, given_mst):
    g = Graph(n)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])

    mst = g.kruskal_mst()
    mst_set = set(given_mst)
    mst_set_generated = set(mst)

    if mst_set == mst_set_generated:
        return True, None
    else:

n = 4
m = 5
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
given_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

is_unique, alternative_mst = is_mst_unique(n, m, edges, given_mst)
print(f"Is the given MST unique? {is_unique}")
if alternative_mst:
    print("Another possible MST:", alternative_mst)
