from django.core.exceptions import ObjectDoesNotExist

from chess_pieces.models import ChessBoard


class ChessBoardDAO:
    """Data access object for chess pieces model."""

    @staticmethod
    def get_all():
        try:
            chess_board = ChessBoard.objects.all()
            return [one_chess_board for one_chess_board in chess_board]
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0])

    @staticmethod
    def get_by_id(primary_key: int):
        try:
            chess_board = ChessBoard.objects.get(id=primary_key)
            return chess_board
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], primary_key)
