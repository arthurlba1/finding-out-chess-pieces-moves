from itertools import product
from typing import List
from typing import Union

from django.core.exceptions import ObjectDoesNotExist

from chess_pieces.constants import ChessPiecesDTOConstants
from chess_pieces.constants.model_constants import ChessPieceConstants
from chess_pieces.helpers import ChessPiecesMovesHelpers
from chess_pieces.models import ChessPiece
from chess_pieces.dao import ChessPiecesDAO

KNIGHT_MOVEMENTS = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
WHITE_PAWN_MOVEMENTS = [[0, -1]]
BLACK_PAWN_MOVEMENTS = [[0, 1]]


class ChessPiecesBO:
    """Chess pieces BO"""

    @staticmethod
    def get_by_id(primary_key: int) -> Union[ChessPiece, dict]:
        return ChessPiecesDAO.get_by_id(primary_key)

    @staticmethod
    def get_all() -> List[ChessPiece]:
        return ChessPiecesDAO.get_all()

    @staticmethod
    def filter_id(name: str, color: str) -> int:
        try:
            chess_piece = ChessPiece.objects.get(name__iexact=name, color__iexact=color)
            return chess_piece.id
        except ObjectDoesNotExist as exc:
            raise ObjectDoesNotExist(exc.args[0], name)

    @staticmethod
    def return_id(response_object: object) -> dict:
        response = {
            ChessPiecesDTOConstants.ID_DTO_KEY: response_object.data[ChessPiecesDTOConstants.PRIMARY_KEY_DTO_KEY]
        }
        return response

    @staticmethod
    def get_moves(request_dictionary: dict):
        moves = []
        chess_piece_name = ChessPiecesBO._filter_name_by_id(
            request_dictionary[ChessPiecesDTOConstants.PRIMARY_KEY_DTO_KEY]
        )

        if chess_piece_name == ChessPieceConstants.KNIGHT:
            moves = ChessPiecesMovesHelpers.get_defined_moves_set(request_dictionary['cell'], KNIGHT_MOVEMENTS)
            for position in moves:
                moves = moves + ChessPiecesMovesHelpers.get_defined_moves_set(position, KNIGHT_MOVEMENTS)

        moves_set = list(set(moves))
        moves_set.sort()
        response = {'moves': moves_set}
        return response

    @staticmethod
    def _filter_name_by_id(primary_key: int) -> str:
        chess_piece_model = ChessPiecesBO.get_by_id(primary_key)
        return chess_piece_model.name
