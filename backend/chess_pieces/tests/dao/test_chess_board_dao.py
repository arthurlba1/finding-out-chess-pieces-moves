from django.test import TestCase

from chess_pieces.tests.helpers import ChessFactoryHelper
from chess_pieces.dao import ChessBoardDAO


class TestChessBoardDAO(TestCase):
    """Test chess pieces dao."""

    def setUp(self):
        self.chess_board_model_one = ChessFactoryHelper.build_and_save_chess_board()
        self.chess_board_model_two = ChessFactoryHelper.build_and_save_chess_board()

    def test_chess_board_equal_different_pk(self):
        self.assertNotEqual(self.chess_board_model_one, self.chess_board_model_two)

    def test_chess_piece_equal_rows(self):
        self.assertEqual(self.chess_board_model_one.rows, self.chess_board_model_two.rows)

    def test_chess_piece_equal_name(self):
        self.assertEqual(self.chess_board_model_one.columns, self.chess_board_model_two.columns)

    def test_get_by_id(self):
        chess_piece_model = ChessBoardDAO.get_by_id(self.chess_board_model_one.pk)
        self.assertEqual(chess_piece_model, self.chess_board_model_one)
