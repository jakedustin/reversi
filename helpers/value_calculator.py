import helpers.move_locator as ml


class ValueCalculator:
    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}

    def calculate_value_of_move(self, board, move):
        locator = ml.MoveLocator()
        # get score for player 1 and 2
        score1, score2 = self.calculate_score(board)
        # get values for dictionary
        # corner = np.array([[0,0], [7,0],[0,7], [7,7]])
        # cornerAdjacent = np.array([[0,1], [1,1], [1,0], [6,0],[6,1],[7,1], [0,6], [1,6], [1,7], [6,6], [6,7], [7,6]])
        # edges = np.array([[0,[2:5]], [2:5,0], [7, 2:5], [2:5,7]])

        heuristic_value = ((self.utility["corners"] * locator.is_corner(move)) +
                           (self.utility["adjacentToCorners"] * locator.is_corner_adjacent(move)) +
                           (self.utility["edges"] * locator.is_edge(move)) +
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
