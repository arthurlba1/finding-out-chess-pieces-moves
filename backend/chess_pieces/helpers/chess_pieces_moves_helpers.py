from typing import Tuple


class ChessPiecesMovesHelpers:
    """Chess pieces movement helper."""

    @staticmethod
    def get_defined_moves_set(algebraic_notation: str, move_rules: list):
        moves = []
        column_current_position = algebraic_notation[0]
        row_current_position = int(algebraic_notation[1])

        column_number = ord(column_current_position) - 96

        for move in move_rules:
            moves.append([column_number + move[0], row_current_position + move[1]])

        moves = ChessPiecesMovesHelpers._valid_moves(moves)
        moves = map(ChessPiecesMovesHelpers._convert_to_algebraic, moves)
        return list(moves)

    @staticmethod
    def _convert_to_algebraic(move):
        return chr(move[0] + 96) + str(move[1])

    @staticmethod
    def _valid_moves(moves: list):
        valid = filter(
            lambda check_move:
            1 <= check_move[0] <= 8
            and 1 <= check_move[1] <= 8,
            moves
        )
        return list(valid)
