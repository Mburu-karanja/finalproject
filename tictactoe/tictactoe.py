"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


   # raise NotImplementedError
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    return X if count_X <= count_O else O



  #  raise NotImplementedError
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions



   # raise NotImplementedError
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    current_player = player(board)

    if board[i][j] != EMPTY:
        raise Exception("Invalid action: cell already occupied")

    new_board = [row.copy() for row in board]
    new_board[i][j] = current_player

    return new_board

#    raise NotImplementedError
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    for j in range(3):
        if [board[i][j] for i in range(3)].count(X) == 3:
            return X
        elif [board[i][j] for i in range(3)].count(O) == 3:
            return O

    # Check diagonals
    if [board[i][i] for i in range(3)].count(X) == 3 or [board[i][i] for i in range(3)].count(O) == 3:
        return X if board[1][1] == X else O

    if [board[i][2 - i] for i in range(3)].count(X) == 3 or [board[i][2 - i] for i in range(3)].count(O) == 3:
        return X if board[1][1] == X else O

    return None


    #    raise NotImplementedError
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


 
   # raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


    #raise NotImplementedError
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None

    for action in actions(board):
        _, min_val = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action

    return v, best_action

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val is not None and min_val > v:
            v = min_val
            best_action = action

    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val is not None and max_val < v:
            v = max_val
            best_action = action

    return v, best_action


