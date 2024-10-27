import random

print('==================Welcome to Tic Tac Toe===========')
print()
pos_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = 3
cols = 3

def GameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print('|', end="")
        for y in range(cols):
            print('', game_board[x][y], end="")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    # if(num == 0):
    #     game_board[0][0] = turn
    # elif num == 1:
    #     game_board[0][1] = turn
    # elif num == 2:
    #     game_board[0][2] = turn
    # elif num == 3:
    #     game_board[1][0] = turn
    # elif num == 4:
    #     game_board[1][1] = turn
    # elif num == 5:
    #     game_board[1][2] = turn
    # elif num == 6:
    #     game_board[2][0] = turn
    # elif num == 7:
    #     game_board[2][1] = turn
    # elif num == 8:
    #     game_board[2][2] = turn

    rows, cols = num // 3, num % 3
    game_board[rows][cols] = turn


def checkForEinner(game_board):
    # if game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X':
    #     print('You have won!')
    #     return 'X'
    # elif game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O':
    #     print('You lose!')
    #     return 'O'
    # elif game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X':
    #     print('You have won!')
    #     return 'X'
    # elif game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O':
    #     print('You lose!')
    #     return 'O'
    # elif game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X':
    #     print('You have won!')
    #     return 'X'
    # elif game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O':
    #     print('You lose!')
    #     return 'O'

    winning_patterns = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left
        [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right
    ]

    for patterns in winning_patterns:
        values = [game_board[rows][cols] for row, col in patterns]
        # check for X or O:
        if values == ['X', 'X', 'X']:
            print('You have won!')
            return 'X'
        elif values == ['O', 'O', 'O']:
            print('You Lose!')
            return 'O'
    # if no winner yet
    return None

leave_loop = False
turn = 'x'
tunn_Counter = 0

while not leave_loop:
    ### Player's turn ###
    if tunn_Counter % 2 == 1:
        GameBoard()
        try:
            number_picked = int(input('\nChoose a number [1 - 9]: '))
            if number_picked >1 or number_picked <= 9:
                modifyArray(number_picked, 'X')
                pos_numbers.remove(number_picked)
                tunn_Counter += 1
            else:
                print("Invalide input, please try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    ### computers turn ###
    else:
        computer_choice = random.choice(pos_numbers)
        print('\nComputer Choivce', computer_choice)
        modifyArray(computer_choice, 'O')
        pos_numbers.remove(computer_choice)
        tunn_Counter += 1

    # check for winner after each turn
    winner = checkForEinner(game_board)
    if winner or not pos_numbers:
        GameBoard()
        if not winner:
            print('It\'s a draw')
        leave_loop = True
    