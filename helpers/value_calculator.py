"""calculates the value of a given state"""
import helpers.move_locator as ml


class ValueCalculator:
    """calculates the value of a given state"""
    def __init__(self, player_one, board):
        if player_one:
            self.player_one = True
            self.board = board

    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}

    player_one = False
    board = ""


    # TODO:b
    def modify_utility_and_get_value(self, num_tiles):
        '''modifies the utility function and gets the heuristic value for the provided board and move'''
        if num_tiles < 20:
            self.utility["totalPoints"] = -5
        else:
            self.utility["totalPoints"] = 5

        return self.calculate_value_of_state()


    # TODO: get rid of probably
    def calculate_value_of_state(self):
        '''calculates the value of a provided move using the utility function and the provided board'''
        # get score for player 1 and 2
        score = self.calculate_player_score()

        # TODO: figure out what to do with these
        # heuristic_value = ((self.utility["corners"] * ml.MoveLocator.is_corner(move)) +
        #                    (self.utility["adjacentToCorners"] * ml.MoveLocator.is_corner_adjacent(move)) +
        #                    (self.utility["edges"] * ml.MoveLocator.is_edge(move)) +
        #                    (self.utility["totalPoints"] * score))
        # print(heuristic_value)


    def calculate_player_score(self):
        '''calculates the scores of players one and two given the provided board'''
        player_score = 0
        player = 1
        if not self.player_one:
            player = 2
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    player_score += 1
        return player_score
