def print_board(board):
    print()
    for x in range(0,9,3):
        print(f"{board[x]} | {board[x+1]} | {board[x+2]}")
        if(x < 6):
            print("__|__|__")
    print()

def check_winner(board):
    winner_combinations = [(0,1,2),(3,4,5),(6,7,8),
                           (0,3,6),(1,4,7),(2,5,8),
                           (0,4,8),(2,4,6)]
    for (i,j,k) in winner_combinations:
        if board[i] == board[j] == board[k] != " ":
            return board[i]
    return None

def miniMax(board, isMax):
    winner = check_winner(board)
    if winner:
        return 1 if winner == 'O' else -1
    if " " not in board:
        return 0

    if isMax:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = miniMax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = miniMax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = miniMax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [" "] * 9
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner or " " not in board:
            print(f"{winner or 'Tie'} wins!")
            break
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move not in range(9) or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        board[move] = "X"

        if " " in board and not check_winner(board):
            ai_move = get_best_move(board)
            board[ai_move] = 'O'

play_game()
