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
    winner = None
    b = board(p1, p2)
    while True:
        b.print_header()
        b.print_board()
        move = b.get_move()
        while not b.is_move_valid(move):
            move = b.get_move()
        b.set_move(move)
        if b.is_game_over() or b.is_winning_pattern_found():
            winner = b.get_winner()
            b.print_board()
            print('The Winner is: {}\n Game Over.'.format(winner._name))
            break
        b.swap_player()


if __name__ == "__main__":
    main()
