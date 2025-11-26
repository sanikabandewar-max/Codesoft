#TIC-TAC-TOE (Random AI)

import random

board = [" "] * 9

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==mark for i,j,k in wins)

def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos in range(9) and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid move.")
        except:
            print("Enter a number 1–9.")

def ai_move():
    free = [i for i,v in enumerate(board) if v == " "]
    move = random.choice(free)
    board[move] = "O"
    print(f"AI chooses position {move+1}")

print("TIC-TAC-TOE (EASIEST VERSION)")
print_board()

while True:
    # Human move10
    human_move()
    print_board()

    if check_win("X"):
        print("You are win! ")
        exit()
    if " " not in board:
        print("Draw!")
        exit()

    # AI move
    ai_move()
    print_board()

    if check_win("O"):
        print("AI wins! ")
        exit()
    if " " not in board:
        print("Draw!")
        exit()
        
