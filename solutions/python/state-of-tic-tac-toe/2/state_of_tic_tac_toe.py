def gamestate(board):
    flat_board = "".join(board)
    x_count = flat_board.count("X")
    o_count = flat_board.count("O")    
    x_won = False
    o_won = False
    patterns = [
        ((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)), # Rows
        ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)), # Columns
        ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0)),                      # Diagonals
    ]

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    for (row_1, column_1), (row_2, column_2), (row_3, column_3) in patterns:
        if board[row_1][column_1] == board[row_2][column_2] == board[row_3][column_3] and board[row_1][column_1] != " ":
            if board[row_1][column_1] == "X":
                x_won = True
            if board[row_1][column_1] == "O":
                o_won = True
    if (x_won + o_won > 1) or (x_won and x_count == o_count) or (o_won and x_count > o_count):
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_won or o_won:
        return "win"
    if " " not in flat_board:
        return "draw"
    return "ongoing"
