# Generated by Django 3.2.15 on 2022-09-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChessBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(verbose_name='rows')),
                ('columns', models.IntegerField(verbose_name='columns')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChessPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Bishop', 'Bishop'), ('King', 'King'), ('Knight', 'Knight'), ('Pawn', 'Pawn'), ('Queen', 'Queen'), ('Rook', 'Rook')], max_length=20, verbose_name='Name')),
                ('color', models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White')], max_length=20, verbose_name='Color')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddConstraint(
            model_name='chesspiece',
            constraint=models.CheckConstraint(check=models.Q(('name__in', ['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook'])), name='chess_pieces_chesspiece_name_valid'),
        ),
        migrations.AddConstraint(
            model_name='chesspiece',
            constraint=models.CheckConstraint(check=models.Q(('color__in', ['Black', 'White'])), name='chess_pieces_chesspiece_color_valid'),
        ),
        migrations.AddConstraint(
            model_name='chessboard',
            constraint=models.CheckConstraint(check=models.Q(('rows__gte', 8)), name='row_gte_8'),
        ),
        migrations.AddConstraint(
            model_name='chessboard',
            constraint=models.CheckConstraint(check=models.Q(('columns__gte', 8)), name='columns_gte_8'),
        ),
    ]