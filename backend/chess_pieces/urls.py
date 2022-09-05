from django.conf.urls import url

from chess_pieces.rests import chess_board_viewset
from chess_pieces.rests import chess_pieces_viewset

urlpatterns = [
    url(r'^chess-pieces$', chess_pieces_viewset.chess_pieces_request),
    url(r'^chess-pieces/details/(?P<pk>[0-9]+)$', chess_pieces_viewset.chess_piece_detail),
    url(r'^chess-pieces/moves$', chess_pieces_viewset.chess_piece_retrieve_moves),
    url(r'^chess-board$', chess_board_viewset.chess_board_request),
    url(r'^chess-board/details/(?P<pk>[0-9]+)$', chess_board_viewset.chess_board_detail),
    url(r'^chess-board/(?P<pk>[0-9]+)$', chess_board_viewset.chess_board_update),
]
