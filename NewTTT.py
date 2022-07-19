import random

choices = [1,2,3,4,5,6,7,8,9]
board = [[' ', '|', ' ', '|', ' \n'], ['-', '-', '-', '-', '-\n'], [' ', '|', ' ', '|', ' \n'], ['-', '-', '-', '-', '-\n'], [' ', '|', ' ', '|', ' \n']]


def start(new_board):
    print('The computer (X) will go first')
    print('This is the board')
    for r in new_board:
        for i in r:
            print(i, end = '')

def computer_choice(choices, new_board):
    x = random.choice(choices)
    if x == 1:
        new_board[0][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 2:
        new_board[0][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 3:
        new_board[0][4] = 'X\n'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 4:
        new_board[2][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 5:
        new_board[2][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 6:
        new_board[2][4] = 'X\n'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 7:
        new_board[4][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 8:
        new_board[4][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if x == 9:
        new_board[4][4] = 'X\n'
        for r in board:
            for i in r:
                print(i, end = '')
    choices.remove(x)

def new_computer(new_board):
    if new_board[0][0] == 'X' and new_board[0][2] == 'X' and new_board[0][4] == ' ':
        new_board[0][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][0] == 'X' and new_board[0][4] == 'X' and new_board[0][2] == ' ':
        new_board[0][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][2] == 'X' and new_board[0][4] == 'X' and new_board[0][0] == ' ':
        new_board[0][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][0] == 'X' and new_board[2][2] == 'X' and new_board[2][4] == ' ':
        new_board[2][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][0] == 'X' and new_board[2][4] == 'X' and new_board[2][2] == ' ':
        new_board[2][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][2] == 'X' and new_board[2][4] == 'X' and new_board[2][0] == ' ':
        new_board[2][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[4][0] == 'X' and new_board[4][2] == 'X' and new_board[4][4] == ' ':
        new_board[4][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[4][0] == 'X' and new_board[4][4] == 'X' and new_board[0][2] == ' ':
        new_board[0][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[4][2] == 'X' and new_board[4][4] == 'X' and new_board[4][0] == ' ':
        new_board[4][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][0] == 'X' and new_board[2][0] == 'X' and new_board[4][0] == ' ':
        new_board[4][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][0] == 'X' and new_board[4][0] == 'X' and new_board[2][0] == ' ':
        new_board[2][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][0] == 'X' and new_board[4][0] == 'X' and new_board[0][0] == ' ':
        new_board[0][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][2] == 'X' and new_board[2][2] == 'X' and new_board[4][2] == ' ':
        new_board[4][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][2] == 'X' and new_board[4][2] == 'X' and new_board[2][2] == ' ':
        new_board[2][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][2] == 'X' and new_board[4][2] == 'X' and new_board[0][2] == ' ':
        new_board[0][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][4] == 'X' and new_board[2][4] == 'X' and new_board[4][4] == ' ':
        new_board[4][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][4] == 'X' and new_board[4][4] == 'X' and new_board[2][4] == ' ':
        new_board[2][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][4] == 'X' and new_board[4][4] == 'X' and new_board[0][4] == ' ':
        new_board[0][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][0] == 'X' and new_board[2][2] == 'X' and new_board[4][4] == ' ':
        new_board[4][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][0] == 'X' and new_board[4][4] == 'X' and new_board[2][2] == ' ':
        new_board[2][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][2] == 'X' and new_board[4][4] == 'X' and new_board[0][0] == ' ':
        new_board[0][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][4] == 'X' and new_board[2][2] == 'X' and new_board[4][0] == ' ':
        new_board[4][0] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[0][4] == 'X' and new_board[4][0] == 'X' and new_board[2][2] == ' ':
        new_board[2][2] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    if new_board[2][2] == 'X' and new_board[4][0] == 'X' and new_board[0][4] == ' ':
        new_board[0][4] = 'X'
        for r in board:
            for i in r:
                print(i, end = '')
    return (new_board)

def user_choice(choices, new_board):
    grid_point = int(input('Make a move (1-9)'))
    if grid_point not in choices:
        print('Space taken, choose a new space')
        grid_point = int(input('Make a move (1-9)'))
        if grid_point == 1:
            new_board[0][0] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 2:
            new_board[0][2] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 3:
            new_board[0][4] = 'O\n'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 4:
            new_board[2][0] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 5:
            new_board[2][2] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 6:
            new_board[2][4] = 'O\n'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 7:
            new_board[4][0] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 8:
            new_board[4][2] = 'O'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        if grid_point == 9:
            new_board[4][4] = 'O\n'
            for r in new_board:
                for i in r:
                    print(i, end = '')
        choices.remove(grid_point)
    elif grid_point == 1:
        new_board[0][0] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 2:
        new_board[0][2] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 3:
        new_board[0][4] = 'O\n'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 4:
        new_board[2][0] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 5:
        new_board[2][2] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 6:
        new_board[2][4] = 'O\n'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 7:
        new_board[4][0] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 8:
        new_board[4][2] = 'O'
        for r in new_board:
            for i in r:
                print(i, end='')
    elif grid_point == 9:
        new_board[4][4] = 'O\n'
        for r in new_board:
            for i in r:
                print(i, end='')
    choices.remove(grid_point)
    return (choices, board)

def check_x(board):
    if board[0][0] == 'X' and board[0][2] == 'X' and board[0][4] == 'X\n':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[2][0] == 'X' and board[2][2] == 'X' and board[4][4] == 'X\n':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[4][0] == 'X' and board[4][2] == 'X' and board[4][4] == 'X\n':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[0][0] == 'X' and board[2][0] == 'X' and board[4][0] == 'X':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[0][2] == 'X' and board[2][2] == 'X' and board[4][2] == 'X':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[0][4] == 'X\n' and board[2][4] == 'X\n' and board[4][4] == 'X\n':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[0][4] == 'X\n' and board[2][2] == 'X' and board[4][0] == 'X':
        print('Computer wins')
        print('End of game')
        end_game()
    elif board[0][0] == 'X' and board[2][2] == 'X' and board[4][4] == 'X\n':
        print('Computer wins')
        print('End of game')
        end_game()

def check_o(board):
    if board[0][0] == 'O' and board[0][2] == 'O' and board[0][4] == 'O\n':
        print('You win')
        print('End of game')
        end_game()
    elif board[2][0] == 'O' and board[2][2] == 'O' and board[2][4] == 'O\n':
        print('You win')
        print('End of game')
        end_game()
    elif board[4][0] == 'O' and board[4][2] == 'O' and board[4][4] == 'O\n':
        print('You win')
        print('End of game')
        end_game()
    elif board[0][0] == 'O' and board[2][0] == 'O' and board[4][0] == 'O':
        print('You win')
        print('End of game')
        end_game()
    elif board[0][2] == 'O' and board[2][2] == 'O' and board[4][2] == 'O':
        print('You win')
        print('End of game')
        end_game()
    elif board[0][4] == 'O\n' and board[2][4] == 'O\n' and board[4][4] == 'O\n':
        print('You win')
        print('End of game')
        end_game()
    elif board[0][4] == 'O\n' and board[2][2] == 'O' and board[4][0] == 'O':
        print('You win')
        print('End of game')
        end_game()
    elif board[0][0] == 'O' and board[2][2] == 'O' and board[4][4] == 'O\n':
        print('You win')
        print('End of game')
        end_game()


def end_game():
    exit()

def main():
    start(board)
    choices_1 = 8

    while choices_1 > -1:
        print("Computer's move is...")
        computer_choice(choices, board)
        check_x(board)
        print("Your move is...")
        user_choice(choices, board)
        check_o(board)
        new_computer(board)
        check_x(board)
        choices_1 -= 2
    print("Cat's game")
    print('End of game')
    exit()


if __name__ == '__main__':
    main()