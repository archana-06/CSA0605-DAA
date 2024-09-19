def graph_coloring(edges, n, k):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [-1] * n
    available_colors = [True] * k

    def get_available_color(node):
        for neighbor in graph[node]:
            if colors[neighbor] != -1:
                available_colors[colors[neighbor]] = False
        for color in range(k):
            if available_colors[color]:
                return color
        return -1

    def color_vertex(node, color):
        for i in range(k):
            available_colors[i] = True
        colors[node] = color

    def maximize_your_colors():
        turn = 0
        your_regions = 0
        for node in range(n):
            if colors[node] == -1:
                assigned_color = get_available_color(node)
                color_vertex(node, assigned_color)
                if turn == 0:
                    your_regions += 1
                turn = (turn + 1) % 3
        return your_regions

    your_max_regions = maximize_your_colors()
    print(f"Maximum number of regions you can color: {your_max_regions}")
    print(f"Colors assigned to regions: {colors}")

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
k = 3

graph_coloring(edges, n, k)
