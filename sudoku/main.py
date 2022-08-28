import numpy as np


def sudoku_load():
    sudoku_matrix = np.loadtxt("sudoku.txt", dtype='int', delimiter=',')
    #np.reshape(sudoku_matrix, (9, 9))
    #print(sudoku_matrix)
    #np.savetxt("sudoku.txt", sudoku_matrix, fmt='%d', delimiter=',')
    return sudoku_matrix


def sudoku_find_possible_values(sudoku_matrix, cell_pos):
    row = cell_pos[0]
    col = cell_pos[1]
    values = []
    for v in range(1, 10):
        valid = True
        # check if unique in row
        for j in range(0, 9):
            if sudoku_matrix[row][j] == v:
                valid = False
        # check if unique in column
        for i in range(0, 9):
            if sudoku_matrix[i][col] == v:
                valid = False
        # check if unique in subgrid
        row_subgrid = int(row/3)
        col_subgrid = int(col/3)
        row_range = (row_subgrid*3, row_subgrid*3 + 3)
        col_range = (col_subgrid*3, col_subgrid*3 + 3)
        for i in range(row_range[0], row_range[1]):
            for j in range(col_range[0], col_range[1]):
                if sudoku_matrix[i][j] == v:
                    valid = False

        if valid:
            values.append(v)

    print(cell_pos, values)
    return values


def sudoku_solve(sudoku_matrix, recursion_depth):
    print(f"{recursion_depth=}\n{sudoku_matrix}")

    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_matrix[i][j] == 0:
                values = sudoku_find_possible_values(sudoku_matrix, (i, j))
                for v in values:
                    sudoku_matrix[i][j] = v
                    print(f"solve: {i},{j}={v}")
                    if sudoku_solve(sudoku_matrix, recursion_depth + 1):
                        return True

                sudoku_matrix[i][j] = 0
                return False

    print(f"solved")
    return True


# load and solve sudoku
if __name__ == '__main__':
    sudoku = sudoku_load()
    sudoku_solve(sudoku, 1)
