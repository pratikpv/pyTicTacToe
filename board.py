from player import *


class board:

    def __init__(self, p1: player, p2: player):
        self._p1 = p1
        self._p1 = p2
        self._grid = [['1'] * 3] * 3

    def validate_move(self, pos: int):
        """
        Check if the move chosen by the player is valid.
        :param pos: board position
        :return: True if move is valid, else False
        """
        pass

    def print_board(self):
        """
        print the grid
        :return: None
        """
        self._grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        for i in range(len(self._grid)):
            print('  {0:<1} | {1:<1} | {2:<1}'.format(self._grid[i][0], self._grid[i][1], self._grid[i][2]))
            print(' -----------')
