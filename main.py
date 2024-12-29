from random import randrange

MACHINE_TOKEN = "X"
USER_TOKEN = "O"


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------" * 3, sep="", end="+\n")
    for i in range(len(board)):
        print("|       " * 3, "|", sep="")
        for j in range(len(board[i])):
            print(("|" + " " * 2), board[i][j], (" " * 2), end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def input_valid(token):
    is_valid = False
    if token > 0 and token < 10:
        is_valid = True
    return is_valid


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    token = int(input("Enter a movement: "))
    if not input_valid(token):
        print("Error: Verify the input")
    for i in range(len(board)):
        for j in range(len(board[i])):
            # if token == board[i][j]:
            #   board[i][j] = token
            if board[i][j] != MACHINE_TOKEN:
                board[i][j] = token
            else:
                print("Error: the field is not empty")


def move(board):
    token = int(input("Enter a movement: "))
    if not input_valid(token):
        print("Error: Verify the input")


def make_list_of_free_fields(board):
    empty_positions = []
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != USER_TOKEN and board[i][j] != MACHINE_TOKEN:
                empty_positions.append((i, j))
    return empty_positions


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    print("a")


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_positions = make_list_of_free_fields(board)
    length_tuple = len(free_positions)
    if length_tuple > 0:
        random_pos = randrange(length_tuple)
        board[random_pos][random_pos] = MACHINE_TOKEN


if __name__ == "__main__":
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    free_positions = make_list_of_free_fields(board)
    human_turn = True
    i = len(board) // 2
    j = len(board[0]) // 2
    board[i][j] = MACHINE_TOKEN
    while len(free_positions) != 0:
        print(free_positions)
        display_board(board)
        if human_turn:
            enter_move(board)
            # win = victory_for(board, USER_TOKEN)
        else:
            draw_move(board)
            # win = victory_for(board, MACHINE_TOKEN)
        free_positions = make_list_of_free_fields(board)
