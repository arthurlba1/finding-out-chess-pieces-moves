from django.db import DatabaseError
from django.test import TestCase

from chess_pieces.tests.helpers import ChessFactoryHelper


class TestChessPiece(TestCase):
    """Holds test cases for chess piece."""

    def setUp(self):
        self.chess_piece = ChessFactoryHelper.build_and_save_chess_piece()

    def test_assert_name_not_null(self):
        self.chess_piece.color = None

        with self.assertRaises(DatabaseError):
            self.chess_piece.save()

    def test_assert_different_name(self):
        self.chess_piece.color = 'Castle'

        with self.assertRaises(DatabaseError):
            self.chess_piece.save()

    def test_assert_color_not_null(self):
        self.chess_piece.color = None

        with self.assertRaises(DatabaseError):
            self.chess_piece.save()

    def test_assert_different_color(self):
        self.chess_piece.color = 'blue'.upper()

        with self.assertRaises(DatabaseError):
            self.chess_piece.save()
