from django.db.utils import DatabaseError
from django.test import TestCase

from chess_pieces.tests.helpers import ChessFactoryHelper


class TestChessBoard(TestCase):

    def setUp(self):
        self.chess_board = ChessFactoryHelper.build_and_save_chess_board()

    def test_rows_greater_than_or_equal_eight(self):
        """"Tests a row if it is greater than or equal to eight"""
        self.chess_board.rows = 7

        with self.assertRaises(DatabaseError):
            self.chess_board.save()

    def test_columns_greater_than_or_equal_eight(self):
        """Tests a columns if it is greater tha or equal to eight"""
        self.chess_board.columns = 7

        with self.assertRaises(DatabaseError):
            self.chess_board.save()
