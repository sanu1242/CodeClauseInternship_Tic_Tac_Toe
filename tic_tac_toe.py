
board = [' ' for _ in range(9)]

def board_print():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(player):
    winner_cond = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in winner_cond)

def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def ai_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    board_print()

    while ' ' in board:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if make_move('X', move):
                board_print()
                if check_winner('X'):
                    print("You win!")
                    return
                ai_move()
                print("\nAI made a move:")
                board_print()
                if check_winner('O'):
                    print("AI wins!")
                    return
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("It's a draw!")

play_game()
