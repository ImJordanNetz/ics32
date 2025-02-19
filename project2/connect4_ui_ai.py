import random
import math
import connect4
import time


EMPTY = 0
RED = 1
YELLOW = 2
DROP = 1
POP  = 2

evaluated_positions = {}
def ai_move(state: connect4.GameState) -> tuple[int, int]:
    
    # # print(get_legal_moves(state))
    # move = random.choice(get_legal_moves(state))
    # # print(move)
    # return (move[0], move[1] + 1)
    
    depth = calculate_depth(state)
    print(depth)
    
    global evaluated_positions
    evaluated_positions = {}
    AI_PLAYER = state.turn
    start_time = time.time()
    score, best_move = minimax(state, depth, True, AI_PLAYER, start_time)
    end_time = time.time()
    print(f"took {end_time - start_time:.2f} seconds to think of move")
    return (best_move[0], best_move[1] + 1)




def calculate_depth(state, target_positions=10**6, min_depth=2):

    effective_branching_factor = len(get_legal_moves(state)) * (connect4.columns(state)**1.3 / 10)

    if effective_branching_factor <= 1:
        return min_depth
    depth = int(math.log(target_positions, effective_branching_factor))
    return max(min_depth, depth)


# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
def minimax(state, depth, maximizing, ai_player, start_time):
    global evaluated_positions
    position_key = tuple(tuple(item) for item in state.board)
    if position_key in evaluated_positions:
        return evaluated_positions[position_key], None

    
    if time.time() - start_time > 9:
        return get_eval(state, ai_player), None

    if depth == 0 or is_game_over(state):
        return get_eval(state, ai_player), None

    legal_moves = get_legal_moves(state)
    best_move = None

    if maximizing:
        max_eval = -999999999999
        for move in legal_moves:
            new_state = play_move(state, move)
            eval_score, best_next_move = minimax(new_state, depth - 1, False, ai_player, start_time)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        evaluated_positions[position_key] = max_eval
        return max_eval, best_move
    else:
        min_eval = 999999999999
        for move in legal_moves:
            new_state = play_move(state, move)
            eval_score, best_next_move = minimax(new_state, depth - 1, True, ai_player, start_time)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        evaluated_positions[position_key] = min_eval
        return min_eval, best_move


def is_game_over(state):
    return connect4.winner(state) != connect4.EMPTY or len(get_legal_moves(state)) == 0

def get_eval(state, ai_player):
    winner = connect4.winner(state)
    if winner == ai_player:
        return 1000000
    elif winner != connect4.EMPTY and winner != ai_player:
        return -1000000

    score = 0
    num_cols = len(state.board)
    num_rows = len(state.board[0])
    

    #horizontal
    for row in range(num_rows):
        for col in range(num_cols - 3):
            line = [state.board[c][row] for c in range(col, col + 4)]
            score += score_line(line, ai_player)

    #vertical
    for col in range(num_cols):
        for row in range(num_rows - 3):
            line = [state.board[col][r] for r in range(row, row + 4)]
            score += score_line(line, ai_player)

    # diag 1
    for col in range(num_cols - 3):
        for row in range(num_rows - 3):
            line = [state.board[col + i][row + i] for i in range(4)]
            score += score_line(line, ai_player)

     # diag 2
    for col in range(num_cols - 3):
        for row in range(3, num_rows):
            line = [state.board[col + i][row - i] for i in range(4)]
            score += score_line(line, ai_player)

    return score


def score_line(line, ai_player):
    
    if ai_player == RED:
        opponent = YELLOW
    else:
        opponent = RED
    
    ai_count = line.count(ai_player)
    opp_count = line.count(opponent)


    if ai_count == 3:
        return 100
    elif ai_count == 2:
        return 25
    elif ai_count == 1:
        return 1
    

    if opp_count == 3:
        return -100
    elif opp_count == 2:
        return -25
    elif opp_count == 1:
        return -1
    return 0


def get_legal_moves(state):
    moves = []
    num_cols = connect4.columns(state)
    num_rows = connect4.rows(state)
    middle_col = num_cols // 2
    
    temp_moves = []
    for col in range(num_cols):
        if state.board[col][0] == EMPTY:
            temp_moves.append((DROP, col))
        if state.board[col][num_rows - 1] == state.turn:
            temp_moves.append((POP, col))
    
    # should prioritize middle since depth doesn't go that far
    moves = sorted(temp_moves, key=lambda move: abs(move[1] - middle_col))
    
    return moves

def play_move(state, move) -> connect4.GameState:
    move_type, col = move
    if move_type == DROP:
        return connect4.drop(state, col)
    elif move_type == POP:
        return connect4.pop(state, col)
