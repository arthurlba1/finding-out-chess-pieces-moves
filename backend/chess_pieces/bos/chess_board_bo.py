from typing import List

from django.core.exceptions import ObjectDoesNotExist

from chess_pieces.beans import ChessBoardBean
from chess_pieces.models import ChessBoard


class ChessBoardBO:
    """Chess Board BO."""

    @staticmethod
    def get_by_id(primary_key: int) -> ChessBoardBean:
        try:
            chess_board = ChessBoard.objects.get(id=primary_key)
            return ChessBoardBean.from_model(chess_board)
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], primary_key)

    @staticmethod
    def get_all() -> List[ChessBoardBean]:
        chess_boards = ChessBoard.objects.all()
        return [ChessBoardBean.from_model(chess_board) for chess_board in chess_boards]
