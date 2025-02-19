# connect4_network_client.py
#
# ICS 32 
# Project #2
#
# This executable module implements a networked console version of Connect Four.

import connect4
import connect4_ui
import connect4_ui_ai
import client_short
import socket


def run_console_network() -> None:
    game = connect4_ui.make_new_game()
    grid_rows = connect4.rows(game)
    grid_columns = connect4.columns(game)

    current_player = 1
    server_start_signal = ""
    server_response = ""
    try:
        network_connection = client_short.connect("arcala-1.ics.uci.edu", 8000)
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        return

    setup_message = f"GAME {grid_rows} {grid_columns}"
    client_short.send_message(network_connection, setup_message)
    while server_start_signal != "START":
        server_start_signal = client_short.receive_response(network_connection).strip()

    while connect4.winner(game) == 0:
        print(connect4_ui.print_board(game))
        if current_player:
            game_previous = game
            # check if move was valid
            while game_previous == game:
                player_move = connect4_ui.choose_move(game)
                game = connect4_ui.make_move(game, player_move) 

            client_short.send_message(network_connection, f"USER {player_move[0]} {player_move[1]}")
            server_response = client_short.receive_response(network_connection).strip()  
        else:
            game_previous = game
            while game_previous == game:
                client_short.send_message(network_connection, "MOVE")
                ai_move = int(client_short.receive_response(network_connection).strip())
                client_short.send_message(network_connection, "COLUMN")
                ai_column = int(client_short.receive_response(network_connection).strip())
                print(f"AI Move = {ai_move} {grid_columns}")
                game = connect4_ui.make_move(game, (ai_move, ai_column))                    
        current_player = (current_player + 1) % 2

    print(connect4_ui.print_board(game))
    client_short.close(network_connection)



if __name__ == '__main__':
    run_console_network()
