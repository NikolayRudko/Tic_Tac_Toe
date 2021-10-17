def draw_field(matrix):
    """Draws the field"""
    print('-' * 9)
    for i in range(len(matrix)):
        print('| %s %s %s |' % (matrix[i][0], matrix[i][1], matrix[i][2]))
    print('-' * 9)


def enter_coordinate():
    """Inputs and verifies the data. :return coordinate X ans Y"""
    coordinates = input('Enter the coordinates:').split()
    # checking the numbers of arguments
    if len(coordinates) != 2:
        print('You should enter numbers!')
        return enter_coordinate()
    # checking for int
    if not coordinates[0].isdigit() or not coordinates[0].isdigit():
        print('You should enter numbers!')
        return enter_coordinate()

    coordinate_x, coordinate_y = map(int, coordinates)
    # checking for int range 0< number <4
    if 0 < coordinate_x < 4 and 0 < coordinate_y < 4:
        return coordinate_x - 1, coordinate_y - 1
    else:
        print('Coordinates should be from 1 to 3!')
        return enter_coordinate()


def make_turn(mark, matrix):
    """Writes an 'X' or 'O' in the entered block."""
    line, row = enter_coordinate()

    if matrix[line][row] != 'X' and matrix[line][row] != 'O':
        matrix[line][row] = mark
        draw_field(matrix=matrix)
    else:
        print('This cell is occupied! Choose another one!')
        make_turn(mark=mark, matrix=matrix)


def check_lines(matrix):
    """Checking the match line for a match :returns True if there is at least one filled line."""
    lines = [matrix[0], matrix[1], matrix[2],               # all rows
             [matrix[0][0], matrix[1][0], matrix[2][0]],    # column 1
             [matrix[0][1], matrix[1][1], matrix[2][1]],    # column 2
             [matrix[0][2], matrix[1][2], matrix[2][2]],    # column 3
             [matrix[0][0], matrix[1][1], matrix[2][2]],    # diagonal 1
             [matrix[2][0], matrix[1][1], matrix[0][2]],    # diagonal 2
             ]
    return any([line.count('X') == 3 or line.count('O') == 3 for line in lines])


def check_field(matrix):
    """Checks for empty blocks, :return True if empty blocks exist."""
    return any([' ' in i for i in matrix])


matrix = [[" "] * 3 for i in range(3)]
players = ('X', 'O')  # set of players
player = 1

draw_field(matrix=matrix)
while not (check_lines(matrix=matrix) or not check_field(matrix=matrix)):
    player = (player + 1) % 2  # change players
    player_mark = players[player]
    make_turn(mark=player_mark, matrix=matrix)
if check_lines(matrix=matrix):
    print('%s wins' % players[player])
else:
    print("Draw")