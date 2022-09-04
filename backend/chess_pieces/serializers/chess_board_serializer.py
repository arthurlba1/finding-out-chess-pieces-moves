from rest_framework import serializers

from chess_pieces.models import ChessBoard


class ChessBoardSerializer(serializers.ModelSerializer):
    """Serializes the chess board bean"""

    class Meta:
        model = ChessBoard
        fields = ['columns', 'rows']
