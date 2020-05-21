#Tic Tac Toe Game - Two Player Game

game_board = ['_','_','_','_','_','_','_','_','_']
game_over =False
turn = 'X'
available_sq = [1,2,3,4,5,6,7,8,9]
def print_board():
    for i in range(0,7,3):
        print(game_board[i]+'\t'+game_board[i+1]+'\t'+game_board[i+2])


def push_board(turn1,sq1):
    global turn
    if game_board[sq1-1] == '_':
        game_board[sq-1] = turn1
        turn = 'O' if turn == 'X' else 'X'
    else:
        print("Square Not available.Choose Another Square")

def is_game_over():
    if game_board[0] ==game_board[1] == game_board[2]=='X' or game_board[3] == game_board[4] ==game_board[5]=='X' or game_board[6]== game_board[7] ==game_board[8]=='X'or game_board[0]==game_board[3]==game_board[6]=='X'or game_board[1]==game_board[4]==game_board[7]=='X'or game_board[2]==game_board[5]==game_board[8]=='X'or game_board[0]==game_board[4]==game_board[8]=='X'or game_board[2]==game_board[4]==game_board[6]=='X' :
        return (True,'X')
    elif game_board[0] == game_board[1] == game_board[2] == 'O' or game_board[3] == game_board[4] == game_board[5] == 'O' or game_board[6] == game_board[7] == game_board[8] == 'O' or game_board[0] == game_board[3] == game_board[6] == 'O' or game_board[1] == game_board[4] == game_board[7] == 'O' or game_board[2] == game_board[5] == game_board[8] == 'O' or game_board[0] == game_board[4] == game_board[8] == 'O' or game_board[2] == game_board[4] == game_board[6] == 'O':
        return(True,'O')
    else:
        return (False,'')


def game_draw():
    if '_' not in game_board :
        return True
    else:
        return False


print_board()
while(game_over == False):
    try:
        sq=int(input("Enter a square: "))
    except ValueError:
        print("Enter a number between 1-9")

    if(sq not in available_sq):
        print("Invalid Square Number Entered. Try Again.")
        continue
    else:
        push_board(turn,sq)
    print_board()
    result =is_game_over()
    if(result[0]):
        print("Game Over")
        print(result[1]+ " wins the game.")
        break
    if game_draw():
        print("No more squares available. Game is draw")
        break




