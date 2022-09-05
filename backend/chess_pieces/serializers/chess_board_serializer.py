from rest_framework import serializers

from chess_pieces.models import ChessBoard


class ChessBoardSerializer(serializers.ModelSerializer):
    """Serializes the chess board"""

    class Meta:
        model = ChessBoard
        fields = ['pk', 'columns', 'rows']
