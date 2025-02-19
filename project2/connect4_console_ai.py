# connect4_console_ai.py
#
# ICS 32 Winter 2022
# Project #2
#
# This executable module implements a console-only version of Connect Four.
# The second player is an AI player.

import connect4
import connect4_ui
import connect4_ui_ai


RED = 1
YELLOW = 2

def run_console_ui() -> None:
    game = connect4_ui.make_new_game()
    while connect4.winner(game) == 0:
        print(connect4_ui.print_board(game))
        if game.turn == YELLOW:
            move = connect4_ui_ai.ai_move(game)
        else:
            move = connect4_ui.choose_move(game)
        game = connect4_ui.make_move(game, move)
        
    print(connect4_ui.print_board(game))



if __name__ == '__main__':
    run_console_ui()
