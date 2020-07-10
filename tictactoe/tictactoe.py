"""
Tic Tac Toe Player
"""
import copy
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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    length = len(board)
    for i in range(length):
        for j in range(length):
            if board[i][j] == "X" or board[i][j] == "O":
                count = count + 1
    if count == 9:
        return "over"
    if count % 2 == 0:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):
        raise ValueError("Invalid action.")
    else:
        ResultingBoard = copy.deepcopy(board)
        if player(board) == "X":
            ResultingBoard[action[0]][action[1]] = "X"
        else:
            ResultingBoard[action[0]][action[1]] = "O"

    return ResultingBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (
            board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (
            board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (
            board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (
            board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (
            board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (
            board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (
            board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        return "X"
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (
            board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (
            board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (
            board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (
            board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (
            board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (
            board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (
            board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        return "O"
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    else:
        return 0




def MaxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -737427379378478374
    for action in actions(board):
        v = max(v, MinValue(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v


def MinValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = 737427379378478374
    for action in actions(board):
        v = min(v, MaxValue(result(board, action), alpha, beta))
        beta = min(beta, v)
        if (beta <= alpha):
            break
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    maximum = -9876544282792
    minimum = 987736356373
    alpha = -2837643415347874
    beta = 46876435468435467

    if board == [[EMPTY] * 3] * 3:
        return 0, 0
    finalaction = None
    if player(board) == "X":
        for action in actions(board):
            minval = MinValue(result(board, action), alpha, beta)
            if minval > maximum:
                finalaction = action
                maximum = minval
        return finalaction

    elif player(board) == "O":
        for action in actions(board):
            maxval = MaxValue(result(board, action), alpha, beta)
            if maxval < minimum:
                finalaction = action
                minimum = maxval

        return finalaction
