import copy
from unittest import TestCase
import numpy as np
import reversi as r
import helpers.state_generator as sg


class TestStateGenerator(TestCase):
    test_board = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 2], 
         [0, 0, 0, 0, 0, 0, 1, 0], 
         [0, 0, 0, 0, 0, 1, 0, 0], 
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0], 
         [0, 0, 2, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0]])
    state = r.ReversiGameState(test_board, 2)
    generator = sg

    def test_get_child_state(self):
        # create a copy of the above board
        # manually change the colors to simulate the move
        # run the color changing methods
        # verify they worked
        color_changed_board = copy.deepcopy(self.test_board)
        color_changed_board = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 2], 
         [0, 0, 0, 0, 0, 0, 2, 0], 
         [0, 0, 0, 0, 0, 2, 0, 0], 
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 2, 2, 0, 0, 0], 
         [0, 0, 2, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0]])
        self.generator.change_colors(self.state, 0, 7)
        for i in range(len(self.state.board)):
            for j in range(len(self.state.board[i])):
                TestCase.assertEqual(self, self.state.board[i][j], color_changed_board[i][j])
        print(str(self.state.board))
        print(str(color_changed_board))
