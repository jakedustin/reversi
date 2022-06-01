import reversi as r
import copy


def change_colors(state, row, column):
    turn = state.board[row][column]
    for run in range(-1, 2):
        for rise in range(-1, 2):
            if run == 0 and rise == 0:
                continue
            else:
                x = row + run
                y = column + rise
                while True:
                    if x < 0 or x > 7 or y < 0 or y > 7:
                        break
                    elif state.board[x][y] == 0:
                        break
                    elif state.board[x][y] == turn:
                        break
                    state.board[x][y] = turn
                    x = x + run
                    y = y + rise


def get_child_state(state, move):
    temp_turn = 1 if state.turn == 2 else 2
    new_state = r.ReversiGameState(copy.deepcopy(state.board), temp_turn)
    new_state.board[move[0]][move[1]] = state.turn
    if not 2 < move[0] < 5 and 2 < move[1] < 5:
        change_colors(new_state, move[0], move[1])
    return new_state

