import numpy as np
import random as rand
import math
import reversi
import helpers.move_locator as ml
import helpers.value_calculator as vc


# identify and pick a valid move
# implement minimax
# implement alpha_beta
# define heuristic eval function - check the first 5 moves and pick the best one

class ReversiBot:
    def __init__(self, move_num):
        self.move_num = move_num

    def make_move(self, state):
        """
        This is the only function that needs to be implemented for the lab!
        The bot should take a game state and return a move.

        The parameter "state" is of type ReversiGameState and has two useful
        member variables. The first is "board", which is an 8x8 numpy array
        of 0s, 1s, and 2s. If a spot has a 0 that means it is unoccupied. If
        there is a 1 that means the spot has one of player 1's stones. If
        there is a 2 on the spot that means that spot has one of player 2's
        stones. The other useful member variable is "turn", which is 1 if it's
        player 1's turn and 2 if it's player 2's turn.

        ReversiGameState objects have a nice method called get_valid_moves.
        When you invoke it on a ReversiGameState object a list of valid
        moves for that state is returned in the form of a list of tuples.

        Move should be a tuple (row, col) of the move you want the bot to make.
        """
        valid_moves = state.get_valid_moves()

        # evaluate all the moves in valid_moves and return the best one

        move = rand.choice(valid_moves)  # Moves randomly...for now
        return move

    def find_best_move(self, board):
        best_move = None
        current_move = None
        # for each move in board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # if current move is better than best move:
                # best_move = current_move
                if current_move > best_move:
                    best_move = current_move
        return best_move

    def minimax(self, current_depth, node_index, max_turn, scores, target_depth):
        if current_depth == target_depth:
            return
        if max_turn:
            return max(self.minimax(current_depth + 1, node_index * 2, False, scores, target_depth),
                       self.minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth))
        else:
            return min(self.minimax(current_depth + 1, node_index * 2, True, scores, target_depth),
                       self.minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth))

    def alpha_beta(self, depth, node_index, maximizing_player,
                   values, alpha, beta):
        # if leaf is reached
        if depth == 3:
            return values[node_index]
        if maximizing_player:
            best = - math.inf
            # go through all children left and right
            for i in range(0, 2):
                val = self.alpha_beta(depth + 1, node_index * 2 + i,
                                      False, values, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                # pruning
                if beta <= alpha:
                    break
        else:
            best = math.inf
            for i in range(0, 2):
                val = self.alpha_beta(depth + 1, node_index * 2 + i,
                                      True, values, alpha, beta)
                best = min(val, best)
                beta = min(best, beta)

                if beta <= alpha:
                    break
        return best

    # TODO: move into value_calculator.py
    def get_value_of_state(self, num_tiles, board, move):
        calculator = vc.ValueCalculator()

        if num_tiles < 20:
            # constants from [-10,10]
            # [0]: corners 
            # [1]: adjacent to corners
            # [2]: edges
            # [3]: total number of points for that move
            calculator.utility["totalPoints"] = -5

            # do strategy 1
            # TODO: make strategy self-referential
            return calculator.calculate_value_of_move(board, move)

        else:
            calculator.utility["totalPoints"] = 5
            # do strategy 2
            return calculator.calculate_value_of_move(board, move)

    def can_move(self, current_turn, str):
        if current_turn == 1:
            opp = 2
        else:
            opp = 1

        if str[0] != opp:
            return False

        for i in range(1, 8):
            if str[i] == 0:
                return False
            if str[i] == current_turn:
                return True

        return False

    def is_legal_move(self, current_turn, board, startx, starty):
        if board[startx][starty] != 0:
            return False

        str = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy is None or dx is None:
                    continue
                str[0] = '\0'
                for ctr in range(1, 8):
                    x = startx + ctr * dx
                    y = starty + ctr * dy
                    if 0 <= x < 8 and 0 <= y < 8:
                        str[ctr - 1] = board[x][y]
                    else:
                        str[ctr - 1] = 0
                if self.can_move(current_turn, str):
                    return True

        return False

    def num_valid_moves(self, current_turn, board):
        count = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if self.is_legal_move(current_turn, board, i, j):
                    count += 1
        return count
