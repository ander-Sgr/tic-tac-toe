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
        return
    move_made = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == token:
                board[i][j] = USER_TOKEN
                move_made = True
    if not move_made:
        print("Error: The field is not empty, try again")
               

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
    if sign == USER_TOKEN:
        player = "human"
    elif sign == MACHINE_TOKEN:
        player = "machine"
    else:
        player = None
    cross1 = cross2 = True
    for i in range(len(board)):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return player
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return player
        if board[i][i] != sign:
            cross1 = False
        if board[2 - i][2 - i] != sign:
            cross2 = False
    if cross1 or cross2:
        return player
    return None


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_positions = make_list_of_free_fields(board)
    size = len(free_positions)
    if size > 0:
        r = randrange(size)
        i, j = free_positions[r]
        board[i][j] = MACHINE_TOKEN


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
            winner = victory_for(board, USER_TOKEN)
        else:
            draw_move(board)
            winner = victory_for(board, MACHINE_TOKEN)
        if winner != None:
            break
        human_turn = not human_turn
        free_positions = make_list_of_free_fields(board)
    display_board(board)
    if winner == 'human':
        print("You win!")
    elif winner == 'machine':
        print("You lost, machine wins!")
    else:
        print("Empate")