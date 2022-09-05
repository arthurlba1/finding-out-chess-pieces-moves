from django.test import TestCase

from chess_pieces.tests.helpers import ChessFactoryHelper
from chess_pieces.dao import ChessPiecesDAO


class TestChessPiecesDAO(TestCase):
    """Test chess pieces dao."""

    def setUp(self):
        self.chess_piece_model_one = ChessFactoryHelper.build_and_save_chess_piece()
        self.chess_piece_model_two = ChessFactoryHelper.build_and_save_chess_piece()

    def test_chess_piece_equal_different_pk(self):
        self.assertNotEqual(self.chess_piece_model_one, self.chess_piece_model_two)

    def test_chess_piece_equal_color(self):
        self.assertEqual(self.chess_piece_model_one.color, self.chess_piece_model_two.color)

    def test_chess_piece_equal_name(self):
        self.assertEqual(self.chess_piece_model_one.name, self.chess_piece_model_two.name)

    def test_get_by_id(self):
        chess_piece_model = ChessPiecesDAO.get_by_id(self.chess_piece_model_one.pk)
        self.assertEqual(chess_piece_model, self.chess_piece_model_one)
