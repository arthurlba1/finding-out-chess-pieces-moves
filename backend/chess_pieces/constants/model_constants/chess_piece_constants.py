from chess_pieces.constants.model_constants import BaseModelConstants


class ChessPieceConstants(BaseModelConstants):
    """Class containing the constants of the chess piece."""

    BISHOP = 'Bishop'
    KING = 'King'
    KNIGHT = 'Knight'
    PAWN = 'Pawn'
    QUEEN = 'Queen'
    ROOK = 'Rook'

    CHESS_NAME_CHOICES = (
        (BISHOP, BISHOP),
        (KING, KING),
        (KNIGHT, KNIGHT),
        (PAWN, PAWN),
        (QUEEN, QUEEN),
        (ROOK, ROOK)
    )

    CHESS_CHOICES_LIST = [
        BISHOP,
        KING,
        KNIGHT,
        PAWN,
        QUEEN,
        ROOK
    ]

    BLACK_COLOR = 'Black'
    WHITE_COLOR = 'White'

    COLOR_CHOICES = (
        (BLACK_COLOR, BLACK_COLOR),
        (WHITE_COLOR, WHITE_COLOR)
    )

    COLOR_CHOICES_LIST = [
        BLACK_COLOR,
        WHITE_COLOR
    ]
