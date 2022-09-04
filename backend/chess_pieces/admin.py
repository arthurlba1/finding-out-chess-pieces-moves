from django.contrib import admin

# Register your models here.

from chess_pieces.models import ChessBoard
from chess_pieces.models import ChessPiece

admin.site.register(ChessPiece)
admin.site.register(ChessBoard)
