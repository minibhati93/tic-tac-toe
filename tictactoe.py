__author__ = 'minibhati'

# A simple tic tac toe

import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def check_winner(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def check_all(char):
    if check_winner(char, 0, 1, 2):
        return True
    elif check_winner(char, 3, 4, 5):
        return True
    elif check_winner(char, 6, 7, 8):
        return True
    elif check_winner(char, 0, 3, 6):
        return True
    elif check_winner(char, 1, 4, 7):
        return True
    elif check_winner(char, 2, 5, 8):
        return True
    elif check_winner(char, 2, 4, 6):
        return True
    elif check_winner(char, 0, 4, 8):
        return True


def start_game():
    while True:
        print "\nWhich position you would like to make your move(0-8)?",
        position = int(input())
        # draw_board(position)
        if board[position] != 'X' and board[position] != 'O':
            board[position] = 'X'
            if check_all('X'):
                show_board()
                print "You win!"
                break

            while True:
                opponent = random.randint(0, 8)
                if board[opponent] != 'O' and board[opponent] != 'X':
                    board[opponent] = 'O'
                    print "Let me take! ", opponent, "\n"
                    if check_all('O'):
                        show_board()
                        print "I win!"
                        return
                    break
        else:
            print "This spot is taken!"
        show_board()


def show_board():
    # print "This is what the board looks like"
    print board[0], "|", board[1], "|", board[2]
    print "---------"
    print board[3], "|", board[4], "|", board[5]
    print "---------"
    print board[6], "|", board[7], "|", board[8]


def show_intro():
    print "This is the board"
    print 0, "|", 1, "|", 2
    print "---------"
    print 3, "|", 4, "|", 5
    print "---------"
    print 6, "|", 7, "|", 8


def main():
    show_intro()
    start_game()


if __name__ == "__main__":
    main()