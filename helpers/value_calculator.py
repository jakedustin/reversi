"""calculates the value of a given state"""
import helpers.move_locator as ml


class ValueCalculator:
    """calculates the value of a given state"""

    @staticmethod
    def calculate_state_utility(state, player):
        """returns an integer valuation of the provided state"""
        score = 0
        score += ValueCalculator.calculate_total_points(player, state.board)

        print("calculated a score of " + str(score))
        return score

    @staticmethod
    def calculate_total_points(player, board):
        score = 0
        total_score = 0
        utility = {"edge": 2, "corner": 20, "adjacent": -5}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    continue
                else:
                    value = ml.MoveLocator.get_move_value(i, j, utility)
                    if board[i][j] == player:
                        score += value
                        total_score += 1
                    else:
                        score -= value
                        total_score += 1
        if total_score == 64 and score > 0:
            return 100000
        return score
