import numpy as np

def print_solution(board, n):
    board_visual = np.full((n, n), '_', dtype=str)
    for r, c in enumerate(board):
        board_visual[r][c] = 'Q'
    print("\n".join(" ".join(row) for row in board_visual))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  

def n_queens():
    try:
        n = int(input("Enter the value of N (size of chessboard): "))
        if n < 1:
            print("N must be greater than 0")
            return
        
        board = [-1] * n 
        solutions = []
        solve_n_queens(board, 0, n, solutions)
        
        if solutions:
            print(f"Total Solutions for {n}-Queens: {len(solutions)}\n")
            for idx, sol in enumerate(solutions, 1):
                print(f"Solution {idx}:")
                print_solution(sol, n)
        else:
            print("No solution exists")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    n_queens()
