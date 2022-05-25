
class MoveLocator:

    def is_edge(self, move): 
        if move[0] == 0 or move[0] == 7:
            return int(move[1] < 6 and move[1] > 1)
        elif (move[1] == 0 or move[1] == 7):
            return int(move[0] < 6 and move[0] > 1)

    def is_corner(self, move):
        if move[0] == 0:
            return int(move[1] == 0 or move[1] == 7)
        elif move[0] == 7:
            return int(move[1] == 0 or move[1] == 7)

    def is_corner_adjacent(self, move):
        if move[0] == 0 or move[0] == 7:
            return int(move[1] == 1 or move[1] == 6)
        elif move[0] == 1 or move[0] == 6:
            return (move[1] < 2 or move[1] > 5)