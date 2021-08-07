cells_valid = ["x", "o"]
empty_cell = "_"


def create_matrix(n_row):
    result_matrix = list()
    for index_i in range(n_row):
        row = list()
        for index_j in range(n_row):
            row.append(empty_cell)
        result_matrix.append(row)
    return result_matrix


def is_board_complete(matrix):
    return all(all(cell != empty_cell for cell in row) for row in matrix)


def is_game_continue(matrix):
    # possible winning moves for a 3 x 3 matrix
    winning_moves = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    # check all the winning move
    result_check = list()
    for winning_move in winning_moves:
        partial_result = list()
        for winning_cell in winning_move:
            x = winning_cell[0]
            y = winning_cell[1]
            value_cell = matrix[x][y]
            if len(partial_result) == 0 or (value_cell.lower() in cells_valid and value_cell in partial_result):
                partial_result.append(value_cell)
        if len(partial_result) == len(winning_move):
            result_check.append(partial_result[0])
            break

    is_continue = True

    if len(result_check) > 0:
        print(f"{result_check[0]} wins")
        is_continue = False
    elif len(result_check) == 0 and is_board_complete(matrix):
        print("Draw")
        is_continue = False
    return is_continue


def print_board(matrix):
    print("---------")
    for x in range(len(matrix)):
        print("|", " ".join(matrix[x]).replace(empty_cell, " "), "|")
    print("---------")


def valid_input(user_input, matrix):
    is_valid = True
    # valid if the user's input is a coordinate with 2 positions
    if len(user_input.split()) != 2:
        print("You should enter numbers!")
        is_valid = False
    else:
        user_x, user_y = user_input.split()
        numbers_valid = ["1", "2", "3"]
        # valid if the user's coordinates are numbers
        if not (user_x.isdigit() and user_y.isdigit()):
            print("You should enter numbers!")
            is_valid = False
        # valid if the user's coordinates are numbers between 1 and 3
        elif not (user_x in numbers_valid and user_y in numbers_valid):
            print("Coordinates should be from 1 to 3!")
            is_valid = False
        # valid if the user's coordinates are not occupied on the matrix
        elif matrix[int(user_x) - 1][int(user_y) - 1].lower() in cells_valid:
            print("This cell is occupied! Choose another one!")
            is_valid = False

    return is_valid


def init_game():
    n_row = 3
    # create a matrix for an easier evaluation
    matrix_game = create_matrix(n_row)

    # initialize board
    print_board(matrix_game)
    x_first = True

    # start game
    while is_game_continue(matrix_game):
        user_coordinates = input("Enter the coordinates: ")
        while not (valid_input(user_coordinates, matrix_game)):
            user_coordinates = input("Enter the coordinates: ")
        else:
            # set the user's position on the board
            user_x, user_y = user_coordinates.split()
            user_x = int(user_x) - 1
            user_y = int(user_y) - 1
            matrix_game[user_x][user_y] = "X" if x_first else "O"
            x_first = not x_first

            # print board again
            print_board(matrix_game)


init_game()
