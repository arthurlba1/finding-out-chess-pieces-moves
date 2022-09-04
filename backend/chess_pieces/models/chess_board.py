from django.db import models

from chess_pieces.constants.model_constants import BaseModelConstants


class ChessBoard(models.Model):
    """Chess board model."""

    rows = models.IntegerField(verbose_name='rows')
    columns = models.IntegerField(verbose_name='columns')

    class Meta:
        ordering = [BaseModelConstants.ID_FIELD_KEY]

        constraints = [
            models.CheckConstraint(
                check=models.Q(rows__gte=8),
                name='row_gte_8'
            ),
            models.CheckConstraint(
                check=models.Q(columns__gte=8),
                name='columns_gte_8'
            ),
        ]
