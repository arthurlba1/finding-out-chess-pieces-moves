from chess_pieces.models import ChessBoard


class ChessBoardBean:
    """Chess board bean."""

    def __init__(
        self,
        columns: int,
        primary_key: int,
        rows: int
    ):
        self._columns = columns
        self._id = primary_key
        self._rows = rows

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def matrix(self) -> int:
        return self._rows * self._columns

    @staticmethod
    def from_model(chess_board: ChessBoard):
        return ChessBoardBean(
            columns=chess_board.columns,
            primary_key=chess_board.id,
            rows=chess_board.rows
        )

    def to_dto(self) -> dict:
        return {
            'columns': self.columns,
            'id': self._id,
            'rows': self.rows,
            'matrix': self.matrix
        }
