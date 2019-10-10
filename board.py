from player import *


class board:

    def __init__(self, p1: player, p2: player):
        self._p1 = p1
        self._p2 = p2
        self._grid = [' '] * 10
        # player 1 starts first
        self._turn = p1

    def print_board(self):
        """
        print the grid
        :return: None
        """
        for i in range(1, 4):
            # print('  {0:<1} | {1:<1} | {2:<1}'.format(self._grid[3 * (i - 1) + 0], self._grid[3 * (i - 1) + 1],
            print('  {} | {} | {}'.format(self._grid[3 * (i - 1) + 1], self._grid[3 * (i - 1) + 2],
                                          self._grid[3 * (i - 1) + 3]))
            if i < 3:
                print(' -----------')

    def print_header(self):
        """
        print the grid
        :return: None
        """
        print('Sample board layout')
        sample_grid = list(range(10))
        for i in range(1, 4):
            # print('  {0:<1} | {1:<1} | {2:<1}'.format(sample_grid[i][0], sample_grid[i][1], sample_grid[i][2]))
            print('  {0:<1} | {1:<1} | {2:<1}'.format(sample_grid[3 * (i - 1) + 1], sample_grid[3 * (i - 1) + 2],
                                                      sample_grid[3 * (i - 1) + 3]))
            if i < 3:
                print(' -----------')

        print('Its turn of:{} (symbol: {})'.format(self._turn._name, self._turn._symbol))

    def is_game_over(self):
        """

        :return: True if game is over, else False
        """
        return ' ' not in self._grid

    def get_winner(self):
        """

        :return: player object who won the game
        """
        # for now
        return self._p1

    def get_move(self):
        return self._turn.get_next_move()

    def is_move_valid(self, pos: int):
        """
        Check if the move chosen by the player is valid.
        :param pos: board position
        :return: True if move is valid, else False
        """
        return self._grid[pos] == ' '

    def set_move(self, pos: int):
        if self.is_move_valid(pos):
            self._grid[pos] = self._turn._symbol
            # swap the turns now
            if self._turn == self._p1:
                self._turn = self._p2
            else:
                self._turn = self._p1
        else:
            raise Exception('Invalid move')
