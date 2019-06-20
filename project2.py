## Project 2: Connect Four - Console only ##
## fely magaoay 27278238 & andrel11 16436720 ##

import connectfour


def main():
    '''Runs the console-mode of connect four game'''
    new_game = connectfour.new_game()
    while True:
        print_board(new_game)
        new_game = askinput(new_game)
        x = connectfour.winner(new_game)
        if x == connectfour.RED:
            print("The Winner Is RED.")
            break
        elif x == connectfour.YELLOW:
            print("The Winner Is YELLOW.")
            break
    game_ends(new_game)
    
#make board
def print_board(game_state: connectfour.GameState):
    '''Creates 6x7 board'''
    
    print('1 2 3 4 5 6 7')
    for row in range(connectfour.BOARD_ROWS):
        x = ""
        for column in range(connectfour.BOARD_COLUMNS):
            if game_state.board[column][row] == connectfour.NONE:
                x += '.'  + ' '
            elif game_state.board[column][row] == connectfour.RED:
                x += 'R' + ' '
            elif game_state.board[column][row] == connectfour.YELLOW:
                x += 'Y'  + ' '
        print(x)

    
#ask input/column number (1-7)
def askinput(game_state: connectfour.GameState):
    '''User is asked to specify a move (drop or pop) with the column number'''
    while True:
        if game_state.turn == connectfour.RED:
            move = input("Red player DROP or POP: ")
            player = int(input("Red player column 1-7: "))

        
            if move == 'DROP':
                return connectfour.drop(game_state, player-1)

            else:
                return connectfour.pop(game_state, player-1)
        else:
            move = input("Yellow player DROP or POP: ")
            player = int(input("Yellow player column 1-7: "))
                    
            if move == 'DROP':
                return connectfour.drop(game_state, player-1)
                
            else:
                return connectfour.pop(game_state, player-1)

#game ends
def game_ends(game_state: connectfour.GameState):
    '''When a winner is announced, prints game over'''
    x = connectfour.winner(game_state)
    if x == connectfour.RED or connectfour.YELLOW:
        print("GameOver!!")

#invalid moves



if __name__ == '__main__':
        main()
