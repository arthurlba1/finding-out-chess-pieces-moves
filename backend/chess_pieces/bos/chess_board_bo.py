from typing import List, Union

from chess_pieces.dao import ChessBoardDAO
from chess_pieces.models import ChessBoard


class ChessBoardBO:
    """Chess Board BO."""

    @staticmethod
    def get_by_id(primary_key: int) -> Union[ChessBoard, dict]:
        return ChessBoardDAO.get_by_id(primary_key)

    @staticmethod
    def get_all() -> List[ChessBoard]:
        return ChessBoardDAO.get_all()
