from rest_framework import serializers

from chess_pieces.beans import ChessBoardBean


class ChessBoardSerializer(serializers.ModelSerializer):
    """Serializes the chess board bean"""

    class Meta:
        model = ChessBoardBean
        fields = ['id', 'columns', 'rows']
