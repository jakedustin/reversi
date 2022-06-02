import helpers.state_generator as sg
import helpers.value_calculator as vc


# identify and pick a valid move
# implement minimax
# implement alpha_beta
# define heuristic eval function - check the first 5 moves and pick the best one

class ReversiBot:
    max_depth = 5
    state_generator = sg

    utility = {"corners": 10,
               "adjacentToCorners": -10,
               "edges": 8,
               "totalPoints": 0}

    def __init__(self, move_num):
        self.move_num = move_num

    def make_move(self, state):
        minimax_dict = self.minimax(state, 0, (-1, -1,), float('-inf'), float('inf'))
        return minimax_dict["move"]

    def minimax(self, state, depth, move, alpha, beta):
        valid_moves = state.get_valid_moves()
        print("generated\t" + str(len(valid_moves)) + "\tvalid moves at depth " + str(depth))

        if len(valid_moves) == 0:
            return{"val": 0, "move": (-1, -1)}

        if depth == self.max_depth:
            return {"val": vc.ValueCalculator.calculate_state_utility(state, state.turn), "move": move}

        if depth % 2 == 0:
            best_val = float('-inf')
            i = 0
            for new_move in valid_moves:
                print("reading down branch " + str(i))
                i += 1
                child_state = self.state_generator.get_child_state(state, new_move)
                # print("Calling minimax with: ")
                # print("state: ")
                # print(str(child_state.board))
                # print("depth: " + str(depth + 1))
                # print("move: " + str(move))
                minimax_dict = self.minimax(child_state, depth + 1, new_move, alpha, beta)
                # print("minimax returned: " + minimax_dict.__str__())
                best_val = max(best_val, minimax_dict["val"])
                alpha = max(best_val, alpha)
                if beta <= alpha:
                    print(str(beta) + " <= " + str(alpha))
                    break
            return {"val": best_val, "move": new_move}
        else:
            best_val = float('inf')
            i = 0
            for new_move in valid_moves:
                print("reading down branch " + str(i))
                i += 1
                child_state = self.state_generator.get_child_state(state, new_move)
                # print("Calling minimax with: ")
                # print("state: ")
                # print(str(child_state.board))
                # print("depth: " + str(depth + 1))
                # print("move: " + str(move))
                minimax_dict = self.minimax(child_state, depth + 1, new_move, alpha, beta)
                # print("minimax returned: " + minimax_dict.__str__())
                best_val = min(best_val, minimax_dict["val"])
                beta = min(best_val, beta)
                if beta <= alpha:
                    print(str(beta) + " <= " + str(alpha))
                    break
            return {"val": best_val, "move": new_move}
