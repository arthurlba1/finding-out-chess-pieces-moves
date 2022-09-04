from typing import List

from django.core.exceptions import ObjectDoesNotExist

from chess_pieces.beans import ChessPiecesBean
from chess_pieces.models import ChessPiece


class ChessPiecesBO:
    """Chess pieces BO"""

    @staticmethod
    def get_by_id(primary_key: int) -> ChessPiecesBean:
        try:
            chess_board = ChessPiece.objects.get(id=primary_key)
            return ChessPiecesBean.from_model(chess_board)
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], primary_key)

    @staticmethod
    def get_all() -> List[ChessPiecesBean]:
        try:
            chess_pieces = ChessPiece.objects.all()
            return [ChessPiecesBean.from_model(chess_piece) for chess_piece in chess_pieces]
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0])

    @staticmethod
    def filter_id(name: str, color: str) -> int:
        try:
            chess_piece = ChessPiece.objects.get(name__iexact=name, color__iexact=color)
            return chess_piece.id
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], name)
