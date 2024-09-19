import matplotlib.pyplot as plt
import numpy as np

def plot_board(solution, rows, cols, obstacles=[]):
    board = np.zeros((rows, cols))
    for i in range(len(solution)):
        if solution[i] != -1:
            board[i][solution[i]] = 1
    for obstacle in obstacles:
        board[obstacle[0]][obstacle[1]] = -1

    fig, ax = plt.subplots()
    ax.matshow(board, cmap='gray')

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                ax.text(j, i, 'Q', va='center', ha='center', color='red', fontsize=18)
            elif board[i][j] == -1:
                ax.text(j, i, 'X', va='center', ha='center', color='blue', fontsize=18)

    plt.xticks([])
    plt.yticks([])
    plt.show()

def solve_generalized_nqueens(rows, cols, num_queens, obstacles=[]):
    def is_safe(board, row, col):
        if (row, col) in obstacles:
            return False
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        if row == num_queens:
            solutions.append(board[:])
            return
        for col in range(cols):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
    
    solutions = []
    solve([-1] * rows, 0)
    return solutions

solutions_8x10 = solve_generalized_nqueens(8, 10, 8)
plot_board(solutions_8x10[0], 8, 10)
