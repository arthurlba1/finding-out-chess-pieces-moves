from abc import ABC
from typing import List

from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request

from chess_pieces.beans import ChessPiecesBean
from chess_pieces.bos import ChessPiecesBO
from chess_pieces.models import ChessPiece
from chess_pieces.rests.base_viewset import GenericViewSet
from chess_pieces.rests.base_viewset import Receptor
from chess_pieces.serializers import ChessPiecesSerializer


class ChessPieceViewSet(GenericViewSet, ABC):
    """Chess piece view set."""

    url_basename = 'chess-pieces'
    url_prefix = 'chess-pieces'
    http_method_names = ['get', 'put']
    parser_classes = (MultiPartParser, JSONParser)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bo = ChessPiecesBO

    @Receptor.request_handler
    @action(detail=False)
    def all(self, request: Request) -> List[ChessPiecesBean]:
        return self._bo.get_all()

    @Receptor.request_handler
    @action(methods=['get'], detail=False, url_path='(?P<pk>[^/.]+)')
    def retrieve_by_id(self, request: Request, pk: int) -> ChessPiecesBean:
        return self._bo.get_by_id(pk)

    @Receptor.request_handler
    @action(methods=['get'], detail=False, url_path='(?P<name>[^/.]+)-(?P<color>[^/.]+)')
    def filter_id(self, request: Request, name: str, color: str):
        return self._bo.filter_id(name, color)
