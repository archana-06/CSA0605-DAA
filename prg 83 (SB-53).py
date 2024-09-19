import matplotlib.pyplot as plt
import numpy as np

def plot_board(solution):
    N = len(solution)
    board = np.zeros((N, N))
    for i in range(N):
        board[i][solution[i]] = 1

    fig, ax = plt.subplots()
    ax.matshow(board, cmap='gray')

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ax.text(j, i, 'Q', va='center', ha='center', color='red', fontsize=18)

    plt.xticks([])
    plt.yticks([])
    plt.show()

def solve_nqueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    solve([-1] * n, 0)
    return solutions

solutions_4 = solve_nqueens(4)
solutions_5 = solve_nqueens(5)
solutions_8 = solve_nqueens(8)

plot_board(solutions_4[0])
plot_board(solutions_5[0])
plot_board(solutions_8[0])
