from django.core.exceptions import ObjectDoesNotExist

from chess_pieces.models import ChessPiece


class ChessPiecesDAO:
    """Data access object for chess pieces model."""

    @staticmethod
    def get_all():
        try:
            chess_pieces = ChessPiece.objects.all()
            return [chess_piece for chess_piece in chess_pieces]
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0])

    @staticmethod
    def get_by_id(primary_key: int):
        try:
            chess_board = ChessPiece.objects.get(id=primary_key)
            return chess_board
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], primary_key)
