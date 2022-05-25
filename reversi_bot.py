import numpy as np
import random as rand
import math
import reversi


# identify and pick a valid move
# implement minimax
# implement alpha_beta
# define heuristic eval function - check the first 5 moves and pick the best one


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


    def findBestMove(self, board):
        bestMove = None 
        currentMove = None
        # for each move in board
        for i in range(len(board)):
            for j in range(len(board[i])):
                #if current move is better than best move:
                    # bestMove = currentMove
                    if currentMove > bestMove:
                        bestMove = currentMove
        return bestMove

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

    def alpha_beta(self,depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
            #if leaf is reached 
            if depth == 3:
                return values[nodeIndex]
            if maximizingPlayer:
                best = - math.inf
                # go through all children left and right
                for i in range(0,2):
                    val = self.alpha_beta(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
                    best = max(best, val)
                    alpha = max(alpha, best)
                    #pruning 
                    if beta <= alpha:
                        break
            else:
                best = math.inf
                for i in range(0,2):
                    val = self.alpha_beta(depth + 1, nodeIndex * 2 + i,
                                True, values, alpha, beta)
                    best = min(val, best)
                    beta = min(best, beta)

                    if beta <= alpha:
                        break
            return best
    
    def calcScore(self, board):
        player1 = 0 
        player2 = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    player1 +=1
                elif board[i][j] == 2:
                    player2 += 1
        return player1, player2

    def getValueOfState(self, numTiles):
        
        strategy={"corners": 10,
                "adjacentToCorners":20,
                "edges": 10,
                "totalPoints": 10}

        if numTiles < 20:
            #constants from [-10,10]
            # [0]: corners 
            # [1]: adjacent to corners
            # [2]: edges
            # [3]: total number of points for that move

           
            #do strategy 1
            return self.calculateValueOfMove(strategy, self.board)
            
        else:
            #do strategy 2
            return self.calculateValueOfMove(strategy, self.board)
    
    def calculateValueOfMove(self,strategyDict, board, move):
        #get score for player 1 and 2
        score1, score2 = self.calcScore(board)
        #get values for dictionary
        # corner = np.array([[0,0], [7,0],[0,7], [7,7]])
        # cornerAdjacent = np.array([[0,1], [1,1], [1,0], [6,0],[6,1],[7,1], [0,6], [1,6], [1,7], [6,6], [6,7], [7,6]])
        # edges = np.array([[0,[2:5]], [2:5,0], [7, 2:5], [2:5,7]])

        heuristicValue = (strategyDict["corners"] + strategyDict["adjacentToCorners"] + strategyDict["edges"] + 
        strategyDict["totalPoints"]) * (score1 - score2)

        
        
        

        

    def can_move(self, current_turn, str):
        if current_turn == 1:
            opp = 2
        else:
            opp = 1

        if (str[0] != opp):
            return False

        for i in range(1, 8):
            if (str[i] == 0):
                return False
            if (str[i] == current_turn):
                return True

        return False

    def is_legal_move(self, current_turn, board, startx, starty):
        if (board[startx][starty] != 0):
            return False

        str = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if (dy is None or dx is None):
                    continue
                str[0] = '\0'
                for ctr in range(1, 8):
                    x = startx + ctr*dx
                    y = starty + ctr*dy
                    if (x >= 0 and y >= 0 and x < 8 and y < 8):
                        str[ctr-1] = board[x][y]
                    else:
                        str[ctr-1] = 0
                if (self.can_move(current_turn,str)):
                    return True

        return False

    def num_valid_moves(self, current_turn, board):
        count = 0
        for i in range(0,8):
            for j in range(0,8):
                if (self.is_legal_move(current_turn, board, i, j)):
                    count += 1
        return count


