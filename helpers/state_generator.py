import numpy as np
import reversi as r


class StateGenerator:

    def get_child_state(self, state, move):
        temp_turn = 1 if state.turn == 2 else 2
        new_state = r.ReversiGameState(state.board, temp_turn)
        new_state.board[move[0]][move[1]] = state.turn
        self.change_colors(new_state, move[0], move[1], new_state.turn)
        return new_state
        # TODO: update the whole board, so tiles flip

    def change_colors(self, state, row, column, turn):

        for inc_x in range(-1, 2):
            for inc_y in range(-1, 2):
                if inc_x == 0 and inc_y == 0:
                    continue
                self.check_direction(state, row, column, inc_x, inc_y, turn)

    def check_direction(self, state, row, column, inc_x, inc_y, turn):
        sequence = [0 for i in range(8)]
        sequence_length, r, c = 0, 0, 0

        for i in range(1, 8):
            r = row * inc_y * i
            c = column * inc_x * i

            if r < 0 or r > 7 or c < 0 or c > 7:
                break

            sequence[sequence_length] = state.board[r][c]
            sequence_length += 1

        count = 0
        for i in range(sequence_length):
            if turn == 0:
                if sequence[i] == 2:
                    count += 1
                else:
                    if sequence[i] == 1 and count > 0:
                        count = 20
                    break
            else:
                if sequence[i] == 1:
                    count += 1
                else:
                    if sequence[i] == 2 and count > 0:
                        count = 20
                    break

        if count > 10:
            if turn == 0:
                i = 1
                r = row * inc_y * i
                c = column * inc_x * i
                while state.board[r][c] == 2:
                    state.board[r][c] = 1
                    i += 1
                    r = row * inc_y * i
                    c = column * inc_x * i
            else:
                i = 1
                r = row * inc_y * i
                c = column * inc_x * i
                while state.board[r][c] == 1:
                    state.board[r][c] = 2
                    i += 1
                    r = row * inc_y * i
                    c = column * inc_x * i
