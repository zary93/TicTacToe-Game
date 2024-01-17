def the_table(table):
    for z in table:
        print(" | ".join(z))
        print("-" * 9)


def check_winner():
    global game
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print("We have a winner!")
        game = False
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print("We have a winner!")
        game = False
    for n in range(3):
        if board[n][0] == board[n][1] == board[n][2] != " ":
            print("We have a winner!")
            game = False
        if board[0][n] == board[1][n] == board[2][n] != " ":
            print("We have a winner!")
            game = False


def check_for_draw():
    global game
    if all(board[x][y] != " " for x in range(3) for y in range(3)):
        print("It's a draw!")
        game = False


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
player = "X"
game = True
the_table(board)
while game:
    row = int(input('Choose the row (1, 2, 3): '))
    column = int(input("Chose the column (1,2,3): "))
    row_board = row - 1
    column_board = column - 1
    if 1 <= row <= 3 and 1 <= column <= 3 and board[row_board][column_board] == " ":
        if board[row_board][column_board] == " ":
            board[row_board][column_board] = player
        check_winner()
    else:
        print("Invalid answer! Try Again")
    if game:
        check_for_draw()
    player = "0" if player == "X" else "X"
    the_table(board)
