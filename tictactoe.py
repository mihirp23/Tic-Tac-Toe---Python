
#!/usr/bin/env python

## Mihir Patel
## 2/27/19
## File: tictactoe.py
## Interactive game of Tic Tac Toe
## Python 3

board = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]

# dictionary to hold player's name
players = [{"name":"player1", "mark":"X"},
           {"name":"player2", "mark":"O"}]

##################################################################
def draw_board():
##################################################################
# display the current state of the board
    for i in range (0,3):
        rowstr = ''
        for j in range(0, 3):
            rowstr += '|' + board[i][j]
        rowstr += '|'
        print(rowstr)

# draw_board()

##################################################################
def get_player_choice():
##################################################################
# get mark character from the player


    for i in range(0, 2):
        players[i]['name'] = input(players[i]['name'] + ", enter your name: ")
        while (True):
            mark = input(players[i]['name'] + ", enter your mark: ")
            if (mark != 'X' and mark != 'O'):
                print("Invalid choice, please try again...")
                continue
            else:
                players[i]['mark'] = mark
                break
    
# get_player_choice()

##################################################################
def is_game_won():
##################################################################
# purpose of this function is to determine whether the tic tac
# toe board is in a 'win' formation.
# Returns True if so. Otherwise, false.

    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        # top row
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        # middle row
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        # bottom row
        return True
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        # left column
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        # middle column
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        # right column
        return True
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        # diagonal from top left and ending bottom right
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        # diagonal from bottom left and ending top right
        return True
    else:
        return False
 
# is_game_won()

##################################################################
def is_spot_open_on_board():
##################################################################
# purpose of this function is to check if there are any "open"
# spots left on the tic tac toe board.
# If so, return true. Otherwise, false.

    for i in range (0, 3):
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                return True

    return False
            

# is_spot_open_on_board()

##################################################################
def is_valid_choice(choice):
##################################################################
# return True if the choice is valid on the board

    for i in range(0, 3):
        for j in range(0, 3):
            if choice == board[i][j]:
                return True

    return False

# is_valid_choice()

##################################################################
def set_mark_on_board(choice, mark):
##################################################################
# mark the board with the provided user choice.

    global board
    for i in range(0, 3):
        for j in range(0, 3):
            if choice == board[i][j]:
                board[i][j] = mark
                return
    return

# set_mark_on_board()

##################################################################
def main():
##################################################################
    print("Welcome to my game of tic tac toe!")

    draw_board()
    get_player_choice()
    print("Enter a digit from 1 - 9 to mark the spot on board")

    # set current player to the first player
    current_player = players[0]

    # display the board before game start
    draw_board()
    while(is_spot_open_on_board()):
        choice = input(current_player['name'] + ", your choice: ")

        if is_valid_choice(choice):
            set_mark_on_board(choice, current_player['mark'])
        else:
            print("invalid choice, try again")
            continue

        draw_board()
        if is_game_won():
            print(current_player['name'] + ", you are the winner!!!")
            break

        # player taking turns
        if current_player['name'] == players[0]['name']:
            current_player = players[1]
        else:
            current_player = players[0]
        

    print("Game Over")

# main()
    
if __name__ == "__main__":
    main()
