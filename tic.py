import random
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def check_draw():
    return ' ' not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")

def ai_move():
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'

def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_win('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break
        
        ai_move()
        print_board()
        if check_win('O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()