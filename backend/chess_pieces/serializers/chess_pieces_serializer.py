from rest_framework import serializers

from chess_pieces.constants.model_constants import ChessPieceConstants
from chess_pieces.beans import ChessPiecesBean
from chess_pieces.models import ChessPiece


class ChessPiecesSerializer(serializers.ModelSerializer):
    """Serializes the chess board bean"""
    class Meta:
        model = ChessPiece
        fields = ['pk', 'name', 'color']
