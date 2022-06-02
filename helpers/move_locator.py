"""Helps to determine the location of a given node within the board"""


class MoveLocator:
    """Helps to determine the location of a given node within the board"""

    @staticmethod
    def get_move_value(x, y, utility):
        if MoveLocator.is_edge((x, y,)):
            return utility["edge"]
        if MoveLocator.is_corner((x, y,)):
            return utility["corner"]
        if MoveLocator.is_corner_adjacent((x, y,)):
            return utility["adjacent"]
        return 1

    @staticmethod
    def is_edge(move):
        """
            Returns a 1 if the provided move (tuple(x, y,) 
            is an edge as defined in the utility function)
            else returns 0
        """
        if move[0] == 0 or move[0] == 7:
            return int(6 > move[1] > 1)
        elif move[1] == 0 or move[1] == 7:
            return int(6 > move[0] > 1)

    @staticmethod
    def is_corner(move):
        """
            Returns a 1 if the provided move (tuple(x, y,) 
            is a corner as defined in the utility function)
            else returns 0
        """
        if move[0] == 0:
            return int(move[1] == 0 or move[1] == 7)
        elif move[0] == 7:
            return int(move[1] == 0 or move[1] == 7)

    @staticmethod
    def is_corner_adjacent(move):
        """
            Returns a 1 if the provided move (tuple(x, y,) 
            is corner-adjacent as defined in the utility function)
            else returns 0
        """
        if move[0] == 0 or move[0] == 7:
            return int(move[1] == 1 or move[1] == 6)
        elif move[0] == 1 or move[0] == 6:
            return move[1] < 2 or move[1] > 5
