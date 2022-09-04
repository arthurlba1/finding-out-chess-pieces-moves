from rest_framework import viewsets

from chess_pieces.models import ChessPiece
from chess_pieces.serializers import ChessPiecesSerializer


class ChessPieceViewSet(viewsets.ModelViewSet):
    """Chess piece view set."""

    queryset = ChessPiece.objects.all()
    serializer_class = ChessPiecesSerializer
