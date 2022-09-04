from typing import Any

from chess_pieces.models import ChessBoard
from chess_pieces.models import ChessPiece
from chess_pieces.tests.helpers.constants.model_constants import ChessPieceTestConstants


class ChessFactoryHelper:

    @staticmethod
    def build_chess_board(rows: int = 8, columns: int = 8) -> ChessBoard:
        return ChessBoard(rows=rows, columns=columns)

    @staticmethod
    def build_and_save_chess_board(**kwargs: Any) -> ChessBoard:
        chess_board = ChessFactoryHelper.build_chess_board(**kwargs)
        chess_board.save()
        return chess_board

    @staticmethod
    def build_chess_piece(
            name: str = ChessPieceTestConstants.KING,
            color: str = ChessPieceTestConstants.WHITE_COLOR
    ) -> ChessPiece:
        return ChessPiece(name=name, color=color)

    @staticmethod
    def build_and_save_chess_piece(**kwargs: Any) -> ChessPiece:
        chess_piece = ChessFactoryHelper.build_chess_piece(**kwargs)
        chess_piece.save()
        return chess_piece
