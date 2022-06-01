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
    generator = sg.StateGenerator()

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
        TestCase.assertTrue(np.equal(self.state.board, color_changed_board),
                            "Arguments are not equal: \n" + str(self.test_board) + "\n\n" + str(color_changed_board))
        print(str(self.state.board))
        print(str(color_changed_board))
