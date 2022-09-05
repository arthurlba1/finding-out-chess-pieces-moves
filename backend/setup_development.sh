#!/usr/bin/env bash
python manage.py migrate
echo "from chess_pieces.models.chess_board import ChessBoard; ChessBoard.objects.all().delete(); ChessBoard.objects.create(columns=8, rows=8)" | python manage.py shell
python manage.py runserver
