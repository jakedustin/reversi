import helpers.move_locator as ml


class ValueCalculator:
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

    """
     modifies the utility function and gets the heuristic value for the provided board and move
    """
    # TODO:b
    def modify_utility_and_get_value(self, num_tiles):
        if num_tiles < 20:
            self.utility["totalPoints"] = -5
        else:
            self.utility["totalPoints"] = 5

        return self.calculate_value_of_state()

    """
     calculates the value of a provided move using the utility function and the provided board
    """
    # TODO: get rid of probably
    def calculate_value_of_state(self):
        # get score for player 1 and 2
        score1, score2 = self.calculate_score(board)

        heuristic_value = ((self.utility["corners"] * ml.MoveLocator.is_corner(move)) +
                           (self.utility["adjacentToCorners"] * ml.MoveLocator.is_corner_adjacent(move)) +
                           (self.utility["edges"] * ml.MoveLocator.is_edge(move)) +
                           (self.utility["totalPoints"] * (score1 - score2)))
        print(heuristic_value)

    """
     calculates the scores of players one and two given the provided board
    """
    def calculate_player_score(self):
        player_score = 0
        if self.player_one:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 1:
                        player_score += 1
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 1:
                        player_score += 1
        return player_score
