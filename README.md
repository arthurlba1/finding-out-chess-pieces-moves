
# **Finding out chess pieces moves**

## **Description**

Application that consists of registering chess pieces, or a board larger than the conventional one (8x8).  
In addition, given a location on a coordinate chosen by the user and the piece id,
if it is a knight, find out all possible locations where the knight can move in 2 turns.

## API

Some operations are performed with the api.

- Retrieve all chess pieces.
- Retrieve a chess piece using its id.
- Retrieve a chess piece id using your name and color attribute.
- Retrieve all chess boards.
- Retrieve an array of possible positions of a piece by passing a coordinate (in Algebraic notation) and a chess piece id.

## Technologies

### Backend
- Python
- Django
- Django Rest Framework

## Architecture

Details on the architecture of the project. 

### Backend

![Backend-Architecture](./assets/images/backend_architecture.png)

#### Backend Apps

![Backend-Apps-Architecture](./assets/images/backend_app_architecture.png)

## **How the Algorithm Works**

### General

Basically the algorithm starts by receiving a dictionary that contains the id of the chess piece and a cell from which
it will start. 'get_moves' because it will catch all possible moves, making a query in the model for the piece with the  
corresponding id will already know what the chess piece will be. In general, we will have a method that will take the
algebraic notation piece and the chess piece rule.

~~~python
    def get_moves(request_dictionary: dict):
        moves = []
        chess_piece_name = ChessPiecesBO._filter_name_by_id(
            request_dictionary[ChessPiecesDTOConstants.PRIMARY_KEY_DTO_KEY]
        )
~~~

### Knight

Besides that, we already know that the knight piece can move, at most (it depends on the knight current position),
**8 positions**. The algorithm has these possible moves defined in an array that contains another array
(`[row, column]`) on each position:

~~~python
KNIGHT_MOVEMENTS = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
~~~

Basically this is the chess piece rule.  

The algorithm will run the steps below:
1. It will receive the algebraic notation and the rule of the piece, from there we separate it into 2 variables and
convert the column that's a string to an integer using unicode.  

~~~python
 def get_defined_moves_set(algebraic_notation: str, move_rules: list):
        moves = []
        column_current_position = algebraic_notation[0]
        row_current_position = int(algebraic_notation[1])

        column_number = ord(column_current_position) - 96
~~~

2. We concatenate the current position with the knight rule.

~~~python
        for move in move_rules:
            moves.append([column_number + move[0], row_current_position + move[1]])
~~~

3. The filter is made only with valid positions according to the size of the chessboard (dynamic)

~~~python
    moves = ChessPiecesMovesHelpers._valid_moves(moves)
    
    """Function to filter"""
    def _valid_moves(moves: list):
        chess_board = ChessBoardBO.get_board_size()
        valid = filter(
            lambda check_move:
            1 <= check_move[0] <= chess_board[0]
            and 1 <= check_move[1] <= chess_board[1],
            moves
        )
        return list(valid)
~~~

4. Conversion to algebraic notation is done again and returned to the user.

~~~python
moves = map(ChessPiecesMovesHelpers._convert_to_algebraic, moves)
return list(moves)

"""Function to convert in algebraic notation"""
@staticmethod
    def _convert_to_algebraic(move):
        return chr(move[0] + 96) + str(move[1])
~~~

## License

Licensed under the [MIT License](https://github.com/arthurlba1/finding-out-chess-pieces-moves/blob/master/LICENSE).
