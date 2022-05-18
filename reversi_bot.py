import numpy as np
import random as rand
import math
import reversi


# identify an valid move and pick it 
#implemet minimax
#implement alphabeta
#define heurstic eval function - check the first 5 moves and pick the best one


class ReversiBot:
    def __init__(self, move_num):
        self.move_num = move_num

    def make_move(self, state):
        '''
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
        '''
        valid_moves = state.get_valid_moves()

        #evaluate all the moves in valid_moves and return the best one 

        move = rand.choice(valid_moves) # Moves randomly...for now
        return move


    def minimax(self,curDepth, nodeIndex, maxTurn, scores, targetDepth):
        if curDepth == targetDepth:
            return
        if maxTurn:
            return max(self.minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth),
                   self.minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth))
        else:
            return min(self.minimax(curDepth + 1, nodeIndex * 2,
                     True, scores, targetDepth),
                   self.minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, scores, targetDepth))

    def alphabeta(self,depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
            #if leaf is reached 
            if depth == 3:
                return values[nodeIndex]
            if maximizingPlayer:
                best = - math.inf
                # go through all children left and right
                for i in range(0,2):
                    val = self.alphabeta(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
                    best = max(best, val)
                    alpha = max(alpha, best)
                    #pruning 
                    if beta <= alpha:
                        break
            else:
                best = math.inf
                for i in range(0,2):
                    val = self.alphabeta(depth + 1, nodeIndex * 2 + i,
                                True, values, alpha, beta)
                    best = min(val, best)
                    beta = min(best, beta)

                    if beta <= alpha:
                        break
            return best
