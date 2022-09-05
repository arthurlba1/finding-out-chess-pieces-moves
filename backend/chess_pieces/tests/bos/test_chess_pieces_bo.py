from django.test import TestCase

from chess_pieces.bos import ChessPiecesBO
from chess_pieces.tests.helpers import ChessFactoryHelper
from chess_pieces.tests.helpers.constants.model_constants import ChessPieceTestConstants


class TestChessPiecesBO(TestCase):

    def setUp(self):
        self.chess_piece_knight = ChessFactoryHelper.build_and_save_chess_piece(name=ChessPieceTestConstants.KNIGHT)
        self.knight_with_defined_algebraic_notation = ChessFactoryHelper.build_dictionary(
            self.chess_piece_knight.pk, 'a1'
        )

    def build_move_set(self):
        return ChessPiecesBO.get_moves(self.knight_with_defined_algebraic_notation)

    def test_knight_next_two_movements(self):
        expected_move_set = {"moves": ["a1", "a3", "a5", "b3", "b4", "c1", "c2", "c5", "d2", "d4", "e1", "e3"]}
        move_set = self.build_move_set()
        self.assertEqual(move_set, expected_move_set)
