"""calculates the value of a given state"""
import helpers.move_locator as ml


class ValueCalculator:
    """calculates the value of a given state"""

    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}

    # if corners are empty then the corner adjacent pieces are very negative
    # if corners are not empty then corner adjacent pieces are neutral
    # this board works for the value of a turn, but not the value of a board
    # TODO: write method to calculate the utility of a given state
    @staticmethod
    def calculate_state_utility(state, player):
        """returns an integer valuation of the provided state"""
        score = 0
        score += ValueCalculator.calculate_corner_values(player, state.board, 10)
        score += ValueCalculator.calculate_corner_adjacent_values(player, state.board, -5)

        print("calculated a score of " + str(score))
        return score

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

    @staticmethod
    def calculate_corner_values(player, board, corner_heuristic_value):
        corners = [[0, 0], [0, 7], [7, 0], [7, 7]]
        score = 0
        for corner in corners:
            corner_value = board[corner[0]][corner[1]]
            if corner_value == 0:
                continue
            elif corner_value == player:
                score += corner_heuristic_value
            else:
                score -= corner_heuristic_value
        return score

    @staticmethod
    def calculate_corner_adjacent_values(player, board, corner_adjacent_heuristic_value):
        corners = {1: [0, 0], 2: [0, 7], 3: [7, 0], 4: [7, 7]}

        corner_adjacents = {1: [[0, 1], [1, 0], [1, 1]],
                   2: [[0, 6], [1, 6], [1, 7]],
                   3: [[6, 0], [6, 1], [7, 1]],
                   4: [[6, 6], [6, 7], [7, 6]]}

        score = 0

        for key in corners:
            corner = corners[key]
            if board[corner[0]][corner[1]] == 0:
                # check the adjacent pieces
                for adjacent in corner_adjacents[key]:
                    if board[adjacent[0]][adjacent[1]] == 0:
                        continue
                    elif board[adjacent[0]][adjacent[1]] == player:
                        score += corner_adjacent_heuristic_value
                    else:
                        score -= corner_adjacent_heuristic_value
        return score
