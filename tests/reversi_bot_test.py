import unittest
import board_helpers.move_locator as ml

class ReversiBotTest(unittest.TestCase):
    locator = ml.MoveLocator()

    def test_is_edge(self):
        locator = ml.MoveLocator()
        edge = (0, 0,)
        self.assertFalse(locator.is_edge(edge))

        edge = (0, 2,)
        self.assertTrue(locator.is_edge(edge))

        edge = (3, 7,)
        self.assertTrue(locator.is_edge(edge))

        edge = (0, 7,)
        self.assertFalse(locator.is_edge(edge))
    
    def test_is_corner(self):
        locator = ml.MoveLocator()
        edge = (0, 0,)
        self.assertTrue(locator.is_corner(edge))

        edge = (0, 7,)
        self.assertTrue(locator.is_corner(edge))

        edge = (7, 0,)
        self.assertTrue(locator.is_corner(edge))

        edge = (7, 7,)
        self.assertTrue(locator.is_corner(edge))

        edge = (3, 3,)
        self.assertFalse(locator.is_corner(edge))

if __name__ == '__main__':
    unittest.main()