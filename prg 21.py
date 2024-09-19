"""You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
indicates 2 indices(0-indexed) of the string.You can swap the characters at any pair of indices in the given
pairs any number of times. Return the lexicographically smallest string that s can be changed to after using the swaps."""

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def smallestStringWithSwaps(s, pairs):
    n = len(s)
    uf = UnionFind(n)
    for a, b in pairs:
        uf.union(a, b)
    components = defaultdict(list)
    for i in range(n):
        root = uf.find(i)
        components[root].append(i)
    s_list = list(s)
    for indices in components.values():
        chars = [s_list[i] for i in indices]
        chars.sort()
        for i, char in zip(sorted(indices), chars):
            s_list[i] = char
    
    return ''.join(s_list)
s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  
