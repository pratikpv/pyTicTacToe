from player import *


class board:

    def __init__(self, p1: player, p2: player):
        self._p1 = p1
        self._p2 = p2
        self._grid = [' '] * 10
        self._grid[0] = '#'
        # player 1 starts first
        self._turn = p1

    def print_board(self):
        """
        print the grid
        :return: None
        """
        for i in range(1, 4):
            print('  {0:<1} | {1:<1} | {2:<1}'.format(self._grid[3 * (i - 1) + 1], self._grid[3 * (i - 1) + 2],
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

    def is_winning_pattern_found(self):

        if self._grid[1] == self._grid[2] == self._grid[3] != ' ' or \
                self._grid[4] == self._grid[5] == self._grid[6] != ' ' or \
                self._grid[7] == self._grid[8] == self._grid[9] != ' ' or \
                self._grid[1] == self._grid[4] == self._grid[7] != ' ' or \
                self._grid[2] == self._grid[5] == self._grid[8] != ' ' or \
                self._grid[3] == self._grid[6] == self._grid[9] != ' ' or \
                self._grid[1] == self._grid[5] == self._grid[9] != ' ' or \
                self._grid[3] == self._grid[5] == self._grid[7] != ' ':
            return True

        return False

    def get_winner(self):
        """
        Current player wins when get_winner
        :return: player object who won the game
        """
        return self._turn

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
        else:
            raise Exception('Invalid move')

    def swap_player(self):
        # swap the turns now
        if self._turn == self._p1:
            self._turn = self._p2
        else:
            self._turn = self._p1
