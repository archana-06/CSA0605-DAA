def is_hamiltonian_cycle(graph, path, pos, n):
    if pos == n:
        if path[0] in graph[path[pos - 1]]:
            return True
        else:
            return False

    for v in range(1, n):
        if v in graph[path[pos - 1]] and v not in path:
            path[pos] = v
            if is_hamiltonian_cycle(graph, path, pos + 1, n):
                return True
            path[pos] = -1

    return False

def hamiltonian_cycle(edges, n):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    path = [-1] * n
    path[0] = 0

    if is_hamiltonian_cycle(graph, path, 1, n):
        return True
    else:
        return False

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
n = 5

print(hamiltonian_cycle(edges, n))
