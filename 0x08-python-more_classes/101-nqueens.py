import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N, solutions):
    """
    Utility function to solve the N-queens problem using backtracking.
    """
    if row == N:
        solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_nqueens(N):
    """
    Solve the N-queens problem and print all possible solutions.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    solve_nqueens(sys.argv[1])
