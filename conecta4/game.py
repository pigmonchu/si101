def show(value):
    if value == 1:
        return "x "
    elif value == 2:
        return "0 "
    else:
        return "- "

def show_board(board):
    columns_number = len(board)
    rows_number = len(board[0])
    for row in range(rows_number):
        for column in range(columns_number):
            print(show(board[column][row]), end="")
        print()


columnas = [[0 for _ in range(6)] for i in range(7)]
tablero = columnas

show_board(tablero)
columnas[0][0] = 1
print("*")
show_board(tablero)