# connect4_ui.py
#
# ICS 32 
# Project #2
#
# This module contains utility functions that can be called from a console-
# based UI for a Connect Four game.
# 
# The signatures for the four required functions are provided.
# Hint: It would be useful to create helper functions.

import connect4
from pathlib import Path

RED = 1
YELLOW = 2

DROP = 1
POP = 2

# GameState = namedtuple('GameState', ['board', 'turn'])

def make_new_game() -> connect4.GameState:
    
    
    input_cols = int(input("Columns: "))
    input_rows = int(input("Rows: "))
    game = connect4.new_game(input_cols, input_rows)
    return game

def print_board(state: connect4.GameState) -> str:
    num_cols = connect4.columns(state)
    num_rows = connect4.rows(state)
    board_to_string = ""
    for col in range(num_cols):
        board_to_string += f"{col+1}".ljust(3)
    board_to_string += '\n'
    for row in range(num_rows):
        for col in range(num_cols):
            if state.board[col][row] == 0:
                board_to_string +="."
            if state.board[col][row] == 1:
                board_to_string +="R"
            if state.board[col][row] == 2:
                board_to_string +="Y"
            board_to_string +="  "
        board_to_string +="\n"
    board_to_string +="\n"
    winner = connect4.winner(state)
    if winner == RED:
        board_to_string += "RED wins!\n"
    elif winner == YELLOW:
        board_to_string += "YELLOW wins!\n"
    elif state.turn == RED:
        board_to_string += "RED's turn\n"
    elif state.turn == YELLOW:
        board_to_string += "YELLOW's turn\n"
    return board_to_string + '\n'

def choose_move(state: connect4.GameState) -> tuple[int, int]:
   
    '''
    Asks the user to choose a move, returning a tuple whose first element
    is DROP or POP and whose second element is a valid column number.
    '''

    move_to_int = {
        "d" : DROP,
        "p" : POP
    }
    
    move_type  = input("[D]rop or [P]op? ").lower()
    
    while move_type not in ["d", "p"]:
         move_type  = input("[D]rop or [P]op? ").lower()
    
    move_type_int = move_to_int[move_type]
    
    valid_move = False
    while not valid_move:
        try:
            move_col = int(input("Column: "))
            if connect4._is_valid_column_number(move_col - 1, state.board):
                valid_move = True
            # else:
            #     print("Invalid Move")
        except:
            pass            

    return (move_type_int, move_col)
    
    


def make_move(state: connect4.GameState, move: tuple[int, int]) -> connect4.GameState:
    '''
    Makes the given move against the given state, returning the new state.
    For a valid move, return new state.
    
    Raise connect4.InvalidMoveError if invalid operation detected.
    Implement exception handler to catch this exceptions.
    If connect4.InvalidMoveError exception is caught, return original state inside the exception handler.
    '''

    p = Path(".")
    target_filename = "test_project2.py"  # Change this to the desired filename
    
    move_type = move[0]
    move_col = move[1] - 1
 
    try:
        if move_type == DROP:
            return connect4.drop(state, move_col)
        elif move_type == POP:
            return connect4.pop(state, move_col)
        else:
            print(move)
            raise connect4.InvalidMoveError()
    except connect4.InvalidMoveError:
        print("Invalid Move")
        return state
