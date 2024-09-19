def find_paths(m, n, N, i, j):
    dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
    dp[0][i][j] = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for steps in range(N):
        for x in range(m):
            for y in range(n):
                if dp[steps][x][y] > 0:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            dp[steps + 1][nx][ny] += dp[steps][x][y]
                        else:
                            dp[steps + 1][x][y] += dp[steps][x][y]

    return dp[N][0][0]

# Example usage
print(find_paths(2, 2, 2, 0, 0))
print(find_paths(1, 3, 3, 0, 1))  
