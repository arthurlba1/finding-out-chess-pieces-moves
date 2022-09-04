from typing import List

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.request import Request

from chess_pieces.bos import ChessBoardBO
from chess_pieces.constants.viewset_constants import ViewSetConstants
from chess_pieces.models import ChessBoard
from chess_pieces.serializers import ChessBoardSerializer


@api_view([ViewSetConstants.GET])
def chess_board_request(request: Request):
    if request.method == ViewSetConstants.GET:
        chess_board_model = ChessBoardBO.get_all()
        chess_board_serializer = ChessBoardSerializer(chess_board_model, many=True)
        return JsonResponse(chess_board_serializer.data, safe=False)


@api_view([ViewSetConstants.PATCH])
def chess_board_update(request: Request, pk: int):
    try:
        chess_board_model = ChessBoardBO.get_by_id(pk)
    except ChessBoard.DoesNotExist:
        return JsonResponse({'message': 'The chess piece does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == ViewSetConstants.PATCH:
        chess_board = JSONParser().parse(request)
        chess_board_serializer = ChessBoardSerializer(chess_board_model, data=chess_board)

        if chess_board_serializer.is_valid():
            chess_board_serializer.save()
            return JsonResponse(chess_board_serializer.data)
        return JsonResponse(chess_board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
