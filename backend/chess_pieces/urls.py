from chess_pieces.rests import ChessBoardViewSet
from chess_pieces.rests import ChessPieceViewSet

urlpatterns = [
    ChessBoardViewSet.build_urls(),
    ChessPieceViewSet.build_urls()
]
