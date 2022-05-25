import helpers.move_locator as ml


class ValueCalculator:
    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}

    def calculate_value_of_move(self, board, move):
        # get score for player 1 and 2
        score1, score2 = self.calculate_score(board)

        heuristic_value = ((self.utility["corners"] * ml.MoveLocator.is_corner(move)) +
                           (self.utility["adjacentToCorners"] * ml.MoveLocator.is_corner_adjacent(move)) +
                           (self.utility["edges"] * ml.MoveLocator.is_edge(move)) +
                           (self.utility["totalPoints"] * (score1 - score2)))
        print(heuristic_value)

    def calculate_score(self, board):
        player1 = 0
        player2 = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    player1 += 1
                elif board[i][j] == 2:
                    player2 += 1
        return player1, player2
