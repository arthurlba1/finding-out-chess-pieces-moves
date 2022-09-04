from chess_pieces.models import ChessPiece


class ChessPiecesBean:
    """Chess pieces bean."""

    def __init__(
            self,
            color: str,
            primary_key: int,
            name: str
    ):
        self._color = color
        self._id = primary_key
        self._name = name

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

    @staticmethod
    def from_model(chess_piece: ChessPiece):
        return ChessPiecesBean(
            color=chess_piece.color,
            primary_key=chess_piece.id,
            name=chess_piece.name
        )

    def to_dto(self) -> dict:
        return {
            'color': self.color,
            'id': self._id,
            'name': self.name,
        }
