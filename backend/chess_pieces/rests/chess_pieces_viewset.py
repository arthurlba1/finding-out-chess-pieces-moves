from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.request import Request

from chess_pieces.bos import ChessPiecesBO
from chess_pieces.constants.viewset_constants import ViewSetConstants
from chess_pieces.models import ChessPiece
from chess_pieces.serializers import ChessPiecesSerializer


@api_view([ViewSetConstants.GET, ViewSetConstants.POST])
def chess_pieces_request(request: Request):
    if request.method == ViewSetConstants.GET:
        chess_pieces_model = ChessPiecesBO.get_all()
        chess_pieces_serializer = ChessPiecesSerializer(chess_pieces_model, many=True)
        return JsonResponse(chess_pieces_serializer.data, safe=False)
    elif request.method == ViewSetConstants.POST:
        chess_piece_data = JSONParser().parse(request)
        chess_pieces_serializer = ChessPiecesSerializer(data=chess_piece_data)
        if chess_pieces_serializer.is_valid():
            chess_pieces_serializer.save()
            return JsonResponse(ChessPiecesBO.return_id(chess_pieces_serializer), status=status.HTTP_201_CREATED)
        return JsonResponse(chess_pieces_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ViewSetConstants.GET])
def chess_piece_detail(request, pk):
    try:
        chess_pieces_model = ChessPiecesBO.get_by_id(pk)
    except ChessPiece.DoesNotExist:
        return JsonResponse({'message': 'The chess piece does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == ViewSetConstants.GET:
        chess_pieces_serializer = ChessPiecesSerializer(chess_pieces_model)
        return JsonResponse(chess_pieces_serializer.data)


@api_view([ViewSetConstants.POST])
def chess_piece_retrieve_moves(request):
    chess_piece_data = JSONParser().parse(request)
    return JsonResponse(ChessPiecesBO.get_moves(chess_piece_data), status=status.HTTP_200_OK)

