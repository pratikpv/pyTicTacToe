from player import *
from board import *


def main():
    print('Welcome to Tic Tac Toe!')
    # name = input('Enter player 1 name: ')
    name = 'Player 1'
    p1 = player(name, 'X')
    # name = input('Enter player 2 name: ')
    name = 'Player 2'
    p2 = player(name, '0')

    b = board(p1, p2)
    b.print_board()


if __name__ == "__main__":
    main()
