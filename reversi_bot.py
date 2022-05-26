import numpy as np
import random as rand
import math
import reversi
import helpers.move_locator as ml
import helpers.value_calculator as vc
import helpers.state_generator as sg


# identify and pick a valid move
# implement minimax
# implement alpha_beta
# define heuristic eval function - check the first 5 moves and pick the best one

class ReversiBot:
    max_depth = 5
    # TODO: make state generator static
    state_generator = sg.StateGenerator()

    utility = {"corners": 10,
            "adjacentToCorners": -10,
            "edges": 8,
            "totalPoints": 0}

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
        # TODO: apply all valid moves to copies of the state
        # TODO: do that again and again and again and again and again and again until the heuristic proves true

        # evaluate all the moves in valid_moves and return the best one

        move = rand.choice(valid_moves)  # Moves randomly...for now
        return move

    def minimax(self, state, depth, value, moves_taken):
        valid_moves = state.get_valid_moves()
        print("parent state: ")
        print(str(state.board))

        if depth == self.max_depth:
            # TODO: calculate value of state
            value_state = vc.ValueCalculator.calculate_state_utility(state, self.utility, state.turn)
            # if generated value > value from parent, return value, moves_taken
            if value_state > value:
                return [value_state, moves_taken]
            # else return +-inf, moves_taken
            return [float('inf'), moves_taken]

        # maximize
        if depth % 2 == 0:
            # for move in valid_moves
            for move in valid_moves:
                child_state = self.state_generator.get_child_state(state, move)
                print("child_state: ")
                print(str(child_state.board))
                # get child state
                # temp_value, temp_moves_taken = minimax_temp(self, child_state, depth + 1, math.inf, moves_taken.append(move))
        else:
            # for move in valid_moves
            for i in range(len(valid_moves)):
                print("do something else")
                # temp_value, temp_moves_taken = minimax_temp(self, child_state, depth + 1, -math.inf, moves_taken.append(move))

    # def minimax(self, current_depth, node_index, max_turn, scores, target_depth):
    #     if current_depth == target_depth or current_depth == 0:
    #         # TODO: calculate the value of the board and return the value
    #         score = self.calculator.calculate_player_score()
    #         return score

    #     left_score = self.minimax(current_depth + 1, node_index * 2, False, scores, target_depth)
    #     right_score = self.minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth)

    #     # compare results
    #     if max_turn:
    #         if left_score > right_score:
    #             return left_score
    #         else:
    #             return right_score
    #     else:
    #         if left_score < right_score:
    #             return left_score
    #         else:
    #             return right_score


        #     return max(self.minimax(current_depth + 1, node_index * 2, False, scores, target_depth),
        #                self.minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth))
        # else:
        #     return min(self.minimax(current_depth + 1, node_index * 2, True, scores, target_depth),
        #                self.minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth))

    def alpha_beta(self, depth, node_index, maximizing_player, values, alpha, beta):
        # if leaf is reached
        if depth == 3:
            return values[node_index]
        if maximizing_player:
            best = -math.inf
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





