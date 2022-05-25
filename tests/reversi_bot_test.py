import unittest
import reversi_bot

def is_edge(self, move): 
    if move[0] == 0 or move[0] == 7:
        print('move: ', str(move))
        return move[1] < 6 and move[1] > 1 

class ReversiBotTest(unittest.TestCase):

    def test_is_edge(self):
        edge = (0, 0,)
        self.assertFalse(is_edge(self, edge))

        edge = (0, 2,)
        self.assertTrue(is_edge(self, edge))

if __name__ == '__main__':
    unittest.main()