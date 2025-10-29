import chess  # install python-chess via pip if not already installed
import gzip


def fen_to_question(fen, show_board, show_moves):
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

    if show_moves:
        question += f"The list of legal moves in the Universal Chess Interface (UCI) format is: {', '.join([chess.Move.uci(move) for move in board.legal_moves])}.\n\n"

    question += "Answer with exactly one word, the best move for the side to move, in UCI format.\n"

    return question


with gzip.open("puzzles.epd.gz", "rt") as file:
    for line in file:
        fen, bestmove = line.split(";")
        question = fen_to_question(fen, show_board=True, show_moves=True)
        answer = bestmove.strip()
        print("Question:\n", question)
        print("Answer:\n", answer)
        print("")
