def isSafe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def nqueen(board, row, n, ans):
    if row == n:
        # Make a copy of the board configuration to store in ans
        solution = [''.join(r) for r in board]
        ans.append(solution)
        
        return 

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            nqueen(board, row + 1, n, ans)
            board[row][col] = '.'  # BACKTRACK


# Main
n = 4
ans = []
board = [['.' for _ in range(n)] for _ in range(n)]

nqueen(board, 0, n, ans)

# Print solutions
for solution in ans:
    for row in solution:
        print(row)
    print()
