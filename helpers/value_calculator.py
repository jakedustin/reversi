"""calculates the value of a given state"""
import helpers.move_locator as ml


class ValueCalculator:
    """calculates the value of a given state"""

    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}


    # TODO: write method to calculate the utility of a given state
    @staticmethod
    def calculate_state_utility(state, strategy, player):
        print("calculating state utility")
        """returns an integer valuation of the provided state"""
        score = 0
        print("state.board: \n" + str(state.board))
        for i in range(len(state.board)):
            for j in range(len(state.board[i])):
                if state.board[i][j] == player:
                    score += 1
        return score

    # heuristic_value = ((self.utility["corners"] * ml.MoveLocator.is_corner(move)) +
    #                    (self.utility["adjacentToCorners"] *
    #                       ml.MoveLocator.is_corner_adjacent(move)) +
    #                    (self.utility["edges"] * ml.MoveLocator.is_edge(move)) +
    #                    (self.utility["totalPoints"] * score))
    # print(heuristic_value)


    # TODO: factor in move locator methods
    def calculate_player_score(self, player_one, board):
        '''calculates the scores of players one and two given the provided board'''
        player_score = 0
        player = 1
        if not player_one:
            player = 2
        for i in enumerate(board):
            for j in enumerate(board[i]):
                if board[i][j] == player:
                    player_score += 1
        return player_score
