def print_board(board):
    print()
    for x in range(0,9,3):
        print(f"{board[x]} | {board[x+1]} | {board[x+2]}")
        if(i<6):
            print("___ | ___ | ___")
    print()

def check_winner(board):
    winner_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    for(i,j,k) in winner_combinations:
        if board[i]==board[j]==board[k]!=" ":
            return board[i]
    return None