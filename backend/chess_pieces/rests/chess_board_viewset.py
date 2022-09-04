from rest_framework import viewsets

from chess_pieces.models import ChessBoard
from chess_pieces.serializers import ChessBoardSerializer


class ChessBoardViewSet(viewsets.ModelViewSet):
    """Chess piece view set."""

    queryset = ChessBoard.objects.all()
    serializer_class = ChessBoardSerializer
