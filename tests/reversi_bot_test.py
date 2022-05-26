"""Tests for the reversi bot"""

import unittest
import helpers.move_locator as ml

class ReversiBotTest(unittest.TestCase):
    """Tests for the reversi bot"""
    locator = ml.MoveLocator()

    def test_is_edge(self):
        """Tests for the is_edge method"""
        edge = (0, 0,)
        self.assertFalse(ml.MoveLocator.is_edge(edge))

        edge = (0, 2,)
        self.assertTrue(ml.MoveLocator.is_edge(edge))

        edge = (3, 7,)
        self.assertTrue(ml.MoveLocator.is_edge(edge))

        edge = (0, 7,)
        self.assertFalse(ml.MoveLocator.is_edge(edge))

    def test_is_corner(self):
        """Tests for the is_corner method"""
        edge = (0, 0,)
        self.assertTrue(ml.MoveLocator.is_corner(edge))

        edge = (0, 7,)
        self.assertTrue(ml.MoveLocator.is_corner(edge))

        edge = (7, 0,)
        self.assertTrue(ml.MoveLocator.is_corner(edge))

        edge = (7, 7,)
        self.assertTrue(ml.MoveLocator.is_corner(edge))

        edge = (3, 3,)
        self.assertFalse(ml.MoveLocator.is_corner(edge))

    def test_is_corner_adjacent(self):
        """Tests for the is_corner_adjacent method"""
        edge = (0, 0,)
        self.assertFalse(ml.MoveLocator.is_corner_adjacent(edge))

        edge = (0, 1,)
        self.assertTrue(ml.MoveLocator.is_corner_adjacent(edge))

        edge = (1, 0,)
        self.assertTrue(ml.MoveLocator.is_corner_adjacent(edge))

        edge = (3, 3,)
        self.assertFalse(ml.MoveLocator.is_corner_adjacent(edge))


if __name__ == '__main__':
    unittest.main()
