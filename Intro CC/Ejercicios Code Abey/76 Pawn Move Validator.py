#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Problem Statement
You are to track the sequence of moves in Chess game and check the validity of the pawn moves (other moves are considered correct). As an answer print the number of the incorrect move.

The game is each time started from the initial position:

  +-----------------+
8 | r n b q k b n r |
7 | p p p p p p p p |
6 | - - - - - - - - |
5 | - - - - - - - - |
4 | - - - - - - - - |
3 | - - - - - - - - |
2 | P P P P P P P P |
1 | R N B Q K B N R |
  +-----------------+
    a b c d e f g h
As you see we denote:

white pieces with uppercase letters (P N B R Q K) and black with lowercase (p n b r q k);
pawn with P, kNight with N, bishop with B, rook with R, queen with Q and king with K;
rows with numbers from 1 to 8 and columns with letters from a to h.
The move of a piece is described by its starting and ending coordinate, for example:

e2e4 - white pawn from e2 goes to e4;
g8f6 - black knight from g8 jumps to f6;
d1h5 - white queen from d1 travels to h5 (very stupid move though correct);
f6h5 - black knight from f6 captures the white queen at h5.
After these four moves the position will look like following:

  +-----------------+
8 | r n b q k b - r |
7 | p p p p p p p p |
6 | - - - - - - - - |
5 | - - - - - - - n |
4 | - - - - P - - - |
3 | - - - - - - - - |
2 | P P P P - P P P |
1 | R N B - K B N R |
  +-----------------+
    a b c d e f g h
Pawn move rules
You should check the moves of pawns according to following set of rules:

pawns move only forward, white go from the row 2 up and black go from the row 7 down;
if pawn does not capture anything, it moves straight forward by the same column;
pawn advances exactly one row per move, except the first move when it can optionally go two squares forward (e.g. e2e4 for white or d7d5 for black);
pawn could not move forward if the path is blocked by any piece;
capture is performed by forward diagonal jump by one square to the adjacent column (e.g. e4d5 for white or c7b6 for black) - of course the landing square should be occupied by the enemy piece which is captured.
We do not regard or check the three special cases: the capture "en passant", the promotion of the pawn to other piece at the last row, the move which opens attack on the king or does not remove an existing one (it is illegal).

Input data will contain the number of testcases in the first line.
Next lines will contain one testcase - i.e. one sequence of moves to be checked - each. Of course each sequence should be started from initial position.
Answer should for each sequence tell the number of first incorrect move (starting from 1) or 0 if the whole sequence is valid. Separate answers for different test-cases with spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e76 Pawn Move Validator.txt','r')
P= a.readlines()

movimientos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    movimientos.append(f)

print(movimientos)
"""
movimientos=['f2f4 e7e5 g1f3 e5e4 b1c3 e4f4', 'f2f3 e7e6 g2g4 d8h4 g1h3 h4e1', 'b2b4 b7b5 c1a3 b5b6', 'b1c3 b8c6 b2b2 b7b6', 'e2e4 e7e5 d1f3 g8f6 f2f4 f7f5', 'a2a3 h7h6 b2b4 g7g5 a3a4 h6g5', 'h2h4 g7g4 b1a3 f8h6', 'e2e4 e7e5 e4e5 d8e7 d1e2', 'd2d4 c7c5 d4c5 b7c5', 'e2e4 d7d5 c2c4 d5e4 b1c3 d8d3 c3e4', 'b1c3 b8c6 b2b1 b7b6', 'd2d3 c7c6 d3d4 c6c4 h2h3', 'e2e3 g8h6 d1g4 h6g4 a2a3 b7b6']

def check_pawn_moves(moves):
    board = {
        (1, 'a'): 'R', (1, 'b'): 'N', (1, 'c'): 'B', (1, 'd'): 'Q', (1, 'e'): 'K', (1, 'f'): 'B', (1, 'g'): 'N', (1, 'h'): 'R',
        (2, 'a'): 'P', (2, 'b'): 'P', (2, 'c'): 'P', (2, 'd'): 'P', (2, 'e'): 'P', (2, 'f'): 'P', (2, 'g'): 'P', (2, 'h'): 'P',
        (7, 'a'): 'p', (7, 'b'): 'p', (7, 'c'): 'p', (7, 'd'): 'p', (7, 'e'): 'p', (7, 'f'): 'p', (7, 'g'): 'p', (7, 'h'): 'p',
        (8, 'a'): 'r', (8, 'b'): 'n', (8, 'c'): 'b', (8, 'd'): 'q', (8, 'e'): 'k', (8, 'f'): 'b', (8, 'g'): 'n', (8, 'h'): 'r',
    }

    def parse_position(pos):
        return (int(pos[1]), pos[0])

    def is_pawn_move_valid(start_pos, end_pos, board):
        piece = board.get(start_pos)
        if not piece:
            return False
        if piece.lower() != 'p':
            return True

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if piece == 'P':
            # White pawn
            if start_col == end_col:
                # Moving forward
                if start_row == 2 and end_row == 4 and (3, start_col) not in board and end_pos not in board:
                    return True
                if end_row == start_row + 1 and end_pos not in board:
                    return True
            elif abs(ord(start_col) - ord(end_col)) == 1 and end_row == start_row + 1 and end_pos in board and board[end_pos].islower():
                # Capturing diagonally
                return True
        elif piece == 'p':
            # Black pawn
            if start_col == end_col:
                # Moving forward
                if start_row == 7 and end_row == 5 and (6, start_col) not in board and end_pos not in board:
                    return True
                if end_row == start_row - 1 and end_pos not in board:
                    return True
            elif abs(ord(start_col) - ord(end_col)) == 1 and end_row == start_row - 1 and end_pos in board and board[end_pos].isupper():
                # Capturing diagonally
                return True

        return False

    for move_index, move in enumerate(moves):
        start_pos = parse_position(move[:2])
        end_pos = parse_position(move[2:])

        if not is_pawn_move_valid(start_pos, end_pos, board):
            return move_index + 1

        board[end_pos] = board.pop(start_pos)

    return 0

results = [check_pawn_moves(moves.split()) for moves in movimientos]
print(" ".join(map(str, results)))