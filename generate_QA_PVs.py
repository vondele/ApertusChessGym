import chess  # install python-chess via pip if not already installed
import gzip
import re
import random


def fen_to_question(fen, PV, show_board):
    """
    Turn a FEN, which provides complete information about a chess position,
    into a prompt, helping with both board visualization and move list.
    Alternatively, one could base this also on
    https://github.com/google-deepmind/game_arena/blob/main/game_arena/harness/prompts.py
    """

    board = chess.Board(fen)

    question = f"Given a chess position in Forsyth–Edwards Notation (FEN) notation:\n\n{fen.strip()}\n\n"

    if show_board:
        question += f"Representing the board:\n\n{str(board)}\n\nwith {'white' if board.turn == chess.WHITE else 'black'} to move.\n\n"

    question += "For this position, the Principal Variation (PV) is given by the following moves in Universal Chess Interface (UCI) format. However one move has been masked (_____).\n\n"
    question += f"{' '.join(PV)}\n\n"

    question += "Answer with exactly one word. Which is the move, in UCI format, that is masked in the above PV?\n"

    return question


pattern = re.compile(r"^(.*?) ; .* PV: (.*?)$")

# Given it picks a random move each time, running multiple times will yield different Q&A pairs. 20 rounds are reasonable.
for _ in range(20):
    with gzip.open("caissa_sorted_100000_cdbpv.epd.gz", "rt") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                fen = match.group(1).strip()
                PV = match.group(2).strip(" ;").split()
                if len(PV) < 2:
                    continue

                # Replace a random move in the PV with "_____"
                index = random.randint(0, len(PV) - 1)
                answer = PV[index]
                PV[index] = "_____"

                question = fen_to_question(fen, PV, show_board=True)

                print("Question:\n", question)
                print("Answer:\n", answer)
                print("")
