from typing import TypeVar

from django.db import models
from django.db.models import functions


from chess_pieces.constants.model_constants import ChessPieceConstants


class ChessPiece(models.Model):
    """Chess piece model."""

    name = models.CharField(
        blank=True,
        choices=ChessPieceConstants.CHESS_NAME_CHOICES,
        max_length=20,
        null=False,
        verbose_name='Name'
    )
    color = models.CharField(
        blank=True,
        choices=ChessPieceConstants.COLOR_CHOICES,
        max_length=20,
        null=False,
        verbose_name='Color'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = [ChessPieceConstants.ID_FIELD_KEY]

        models.CharField.register_lookup(functions.Length)
        constraints = [
            models.CheckConstraint(
                check=models.Q(name__in=ChessPieceConstants.CHESS_CHOICES_LIST),
                name='%(app_label)s_%(class)s_name_valid'
            ),
            models.CheckConstraint(
                check=models.Q(color__in=ChessPieceConstants.COLOR_CHOICES_LIST),
                name='%(app_label)s_%(class)s_color_valid'
            )
        ]
