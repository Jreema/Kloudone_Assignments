#Two player Chess Game
import chess
import chess.svg
from IPython.display import SVG
board=chess.Board()
SVG(chess.svg.board(board=board,size=400))
#Prints the chess board
print(board)
global turn1
#Loop continus while game is not over or not stale mate or not check mate
while(board.is_game_over()==False or board.is_stalemate()==False or board.is_checkmate()== False):
    #print(board.legal_moves)
    #GEt input from user
    inp = input("\nEnter the move: ")
    #check if move is a valid move and if so make the move or else print invalid move
    if chess.Move.from_uci(inp) in board.legal_moves:
        board.push_uci(inp)
        print(board)
        if board.turn:
            turn1="White"
            print("\nWhite has to Move")
        else:
            turn1="Black"
            print("\nBlack has to Move")
        #Checks for a check to the King and if so Alerts the King
        if board.is_check():
            print("\nCheck to the King")
            if board.is_checkmate():
                print("Checkmate")
                break;
    else:
        print(board)
        print("\nInvalid Move")

if(board.is_game_over()):
    print("The game is over")
#Checks for a check mate. then sees if white is mated or black is mated
if(board.is_checkmate()):
    if turn1=="White":
        print("White is mated. White has lost the game")
    else:
        print("Black is mated. Black has lost the game")
#checks for a stale mate to see if game is a draw
elif(board.is_stalemate()):
    print("The game is a draw")

