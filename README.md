# ApertusChessGym

generate questions, somewhat configurable, and answers to train LLMs to play chess.

## Example Q&A

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
