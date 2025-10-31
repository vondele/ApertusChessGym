# ApertusChessGym

generate questions, somewhat configurable, and answers to train LLMs to play chess.

## Example Q&A Puzzles

```
Question:
 Given a chess position in Forsyth–Edwards Notation (FEN) notation:

r1bq1rk1/ppp2ppp/5n2/3P4/1P2p3/3BP3/3P1PPP/R1BQK1NR b KQ -

Representing the board:

r . b q . r k .
p p p . . p p p
. . . . . n . .
. . . P . . . .
. P . . p . . .
. . . B P . . .
. . . P . P P P
R . B Q K . N R

with black to move.

The list of legal moves in the Universal Chess Interface (UCI) format is: g8h8, f8e8, d8e8, d8e7, d8d7, d8d6, d8d5, c8d7, c8e6, c8f5, c8g4, c8h3, a8b8, f6e8, f6d7, f6h5, f6d5, f6g4, e4d3, h7h6, g7g6, c7c6, b7b6, a7a6, h7h5, g7g5, c7c5, b7b5, a7a5.

Answer with exactly one word, the best move for the side to move, in UCI format.

Answer:
 e4d3

```

## Example Q&A PV

```
Question:
 Given a chess position in Forsyth–Edwards Notation (FEN) notation:

r1bqkbnr/pp1ppppp/2n5/2p5/8/2N2N2/PPPPPPPP/R1BQKB1R w KQkq -

Representing the board:

r . b q k b n r
p p . p p p p p
. . n . . . . .
. . p . . . . .
. . . . . . . .
. . N . . N . .
P P P P P P P P
R . B Q K B . R

with white to move.

For this position, the Principal Variation (PV) is given by the following moves in Universal Chess Interface (UCI) format. However one move has been masked (_____).

e2e4 g7g6 f1b5 f8g7 _____ d7d6 e1g1 c8d7 h2h3 a7a6 b5c6 d7c6 d3d4 c5d4 f3d4 g8f6 d4c6 b7c6 a1b1 f6d7 c1e3 e8g8 c3a4

Answer with exactly one word. Which is the move, in UCI format, that is masked in the above PV?

Answer:
 d2d3

```
