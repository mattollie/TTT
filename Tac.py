# choices = what spaces are left to choose from
# the_array = the board without any characters required to draw the board



def h_choice(board,choices,the_array):
    ans = str(input('Your choice - Select a number'))
    new_board = board.replace(ans, 'X') # Show the board with the selected choice
    the_array = ['X' if elem == ans else elem for elem in the_array] # Replace the choice with the correct character
    choices.remove(ans) # Get rid of the choice that was selected
    print(new_board)
    return new_board,choices,the_array

def c_choice(board,choices,the_array):
    if len(choices) == 8:
        board,choices,the_array = first_choice(board,choices,the_array)
    elif len(choices) <= 6:
        board,choices,the_array = second_choice(board,choices,the_array)
    print(board)
    return board,choices,the_array

def first_choice(board,choices,the_array):
    if the_array[4] != 'X':
        new_board = board.replace('5', 'O')
        the_array = ['O' if elem == '5' else elem for elem in the_array]
        choices.remove('5')
    else:
        new_board = board.replace('3', 'O')
        the_array = ['O' if elem == '3' else elem for elem in the_array]
        choices.remove('3')
    return new_board,choices,the_array

def second_choice(board,choices,the_array):
    '''Check for h 2 in a row and if it returns true then pick the spot to block. If it returns false, check for c 2
    in a rows that will lead to the most 3 in a row chances'''
    decision = count_double(the_array, 'X')
    decision_Two = count_double(the_array, 'O')
    if decision_Two != False and decision_Two != None:
        new_board = board.replace(str(decision_Two), 'O')
        choices.remove(str(decision))
        the_array = ['O' if elem == decision_Two else elem for elem in the_array]
    elif decision != False and decision != None:
        new_board = board.replace(str(decision), 'O')
        choices.remove(str(decision))
        the_array = ['O' if elem == decision else elem for elem in the_array]
    else:
        decision_One = findbest(the_array, choices)
        new_board = board.replace(str(decision_One), 'O')
        choices.remove(str(decision_One))
        the_array = ['O' if elem == decision_One else elem for elem in the_array]
    return new_board,choices,the_array


def findbest(the_array, choices):
    dict = {}
    for elem in choices:
        counter = 0
        the_array1 = the_array
        the_array1 = ['O' if k == elem else elem for k in the_array1]
        counter = count_double_second(the_array1, 'O', counter)
        choices1 = []
        for i in choices:
            choices1.append(i)
        choices1.remove(elem)
        for elem1 in choices1:
            the_array2 = the_array1
            the_array2 = ['X' if m == elem1 else elem1 for m in the_array2]
            counter = count_double_second(the_array2, 'X', counter)
        dict[elem] = counter
    '''find highest counter/value and return position/key'''
    decision = max(dict, key=lambda k: dict[k])
    return decision


def count_double_second(the_array1, player, counter):
    '''if row/col/diag find double position then counter += 5. At the end, dict.append(position, counter)'''
    '''if player = O then counter += 5 but if player = X then counter -= 5'''
    if player == 'X':
        not_player = 'O'
    else:
        not_player = 'X'
    # Horizontal Check
    for i in range(3):
        x = the_array1[(3*i):((3*i)+3)]
        xone = x.count(player)
        xtwo = x.count(not_player)
        if xone == 2 and xtwo == 0:
            if player == 'O':
                counter += 5
            else:
                counter -= 5
        else:
            continue
    # Vertical Check
    for i in range(3):
        y = the_array1[i:(i+7):3]
        yone = y.count(player)
        ytwo = y.count(not_player)
        if yone == 2 and ytwo == 0:
            if player == 'O':
                counter += 5
            else:
                counter -= 5
        else:
            continue
    # Left to Right Diagonal Check
    z = the_array1[0:9:4]
    zone = z.count(player)
    ztwo = z.count(not_player)
    if zone == 2 and ztwo == 0:
        if player == 'O':
            counter += 5
        else:
            counter -= 5
    # Right to Left Diagonal Check
    a = the_array1[2:7:2]
    aone = a.count(player)
    atwo = a.count(not_player)
    if aone == 2 and atwo == 0:
        if player == 'O':
            counter += 5
        else:
            counter -= 5
    return counter


def count_double(the_array,player):
    if player == 'X':
        not_player = 'O'
    else:
        not_player = 'X'
    # Horizontal Check
    for i in range(3):
        x = the_array[(3*i):((3*i)+3)]
        xone = x.count(player)
        xtwo = x.count(not_player)
        if xone == 2 and xtwo == 0:
            for index, item in enumerate(x):
                if item != player:
                    return item
        else:
            continue
    # Vertical Check
    for i in range(3):
        y = the_array[i:(i+7):3]
        yone = y.count(player)
        ytwo = y.count(not_player)
        if yone == 2 and ytwo == 0:
            for index, item in enumerate(y):
                if item != player:
                    return item
        else:
            continue
    # Left to Right Diagonal Check
    z = the_array[0:9:4]
    zone = z.count(player)
    ztwo = z.count(not_player)
    if zone == 2 and ztwo == 0:
        for index, item in enumerate(z):
            if item != player:
                return item
    # Right to Left Diagonal Check
    a = the_array[2:7:2]
    aone = a.count(player)
    atwo = a.count(not_player)
    if aone == 2 and atwo == 0:
        for index, item in enumerate(a):
            if item != player:
                return item
            else:
                return False

def check_for_win(the_array,choices):
    # Horizontal Check
    for i in range(3):
        x = the_array[(3*i):((3*i)+3)]
        xone = x.count('X')
        xtwo = x.count('O')
        if xone == 3 or xtwo == 3:
            again()
        else:
            continue
    # Vertical Check
    for i in range(3):
        y = the_array[i:(i+7):3]
        yone = y.count('X')
        ytwo = y.count('O')
        if yone == 3 or ytwo == 3:
            again()
        else:
            continue
    # Left to Right Diagonal Check
    z = the_array[0:9:4]
    zone = z.count('X')
    ztwo = z.count('O')
    if zone == 3 or ztwo == 3:
        again()

    # Right to Left Diagonal Check
    a = the_array[2:7:2]
    aone = a.count('X')
    atwo = a.count('O')
    if aone == 3 or atwo == 3:
        again()
    # Check for Cat's game
    elif len(choices) == 0:
        again()
    else:
        return


def again():
    ans = str(input('Game Over! 1 to play again or any character to quit.'))
    main() if ans == '1' else exit(0)

def main():
    # Initial Definitions
    choices = ['1','2','3','4','5','6','7','8','9']
    the_array = choices
    board = '1|2|3\n-|-|-\n4|5|6\n-|-|-\n7|8|9'
    print('Welcome to Tic Tac Toe! You will go first and play as X. Here is the board')
    print(board)

    while True:
        board,choices,the_array = h_choice(board,choices,the_array)
        check_for_win(the_array,choices)
        print('-----------------------')
        board,choices,the_array = c_choice(board,choices,the_array)
        check_for_win(the_array,choices)

if __name__ == '__main__':
    main()
