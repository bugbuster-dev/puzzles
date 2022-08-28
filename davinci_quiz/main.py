import numpy as np


def puzzle_load():
    puzzle_matrix = np.loadtxt("puzzle.txt", dtype='int')
    # solution is an array with a number from each row, last number is current row for solution solving
    solution = np.full(puzzle_matrix.shape[0]+1, -1, dtype='int') # init to -1, -2 used if row contains number in solution
    solution[-1] = 0  # start with row 0
    return puzzle_matrix, solution


def invalid_numbers(puzzle, solution):
    invalid_nums = []
    for i in range(0, puzzle.shape[0]):  # for all rows
        if solution[i] != -1:  # number in that row in solution
            for j in range(0, puzzle.shape[1]):  # for all numbers in that row
                if puzzle[i][j] != solution[i]:  # add to invalid numbers if not solution number
                    invalid_nums.append(puzzle[i][j])

    return invalid_nums


def number_in_solution(puzzle, solution):
    row = solution[-1]
    for i in range(0, puzzle.shape[1]):  # for all numbers in row
        num = puzzle[row][i]
        for j in range(0, puzzle.shape[0]):  # for all numbers in solution
            if num == solution[j]:
                return True

    return False


def update_solution(solution, row, num):
    new_solution = solution.copy()
    new_solution[row] = num
    new_solution[-1] += 1
    return new_solution


def puzzle_solve(puzzle, solution):
    row = solution[-1]
    print("solve row={}, solution={}".format(row, solution))
    if row == puzzle.shape[0]:  # finished last row, check if solved
        n_numbers = 0
        for i in range(0, puzzle.shape[0]):
            if solution[i] >= 0:
                n_numbers += 1

        if n_numbers == 4:  # solution found
            exit(0)
        else:
            return

    if number_in_solution(puzzle, solution):  # check if for current row a number is in solution
        # mark row contains a number of solution and solve next row
        new_solution = update_solution(solution, row, -2)
        puzzle_solve(puzzle, new_solution)
        return

    invalid_nums = invalid_numbers(puzzle, solution)
    # print("invalid numbers={}".format(invalid_nums))
    for i in range(0, puzzle.shape[1]):  # for all numbers in row
        num = puzzle[row][i]
        if num not in invalid_nums:  # number is valid
            # add to solution and solve next row
            new_solution = update_solution(solution, row, num)
            puzzle_solve(puzzle, new_solution)


if __name__ == '__main__':
    puzzle, solution = puzzle_load()
    puzzle_solve(puzzle, solution)
