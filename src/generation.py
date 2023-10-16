from grid import Grid
from solver import set_notes, solve_cell
import random

# generating a puzzle from scratch is very slow. however,
# we can very quickly mutate a solved puzzle to create a
# new puzzle while maintaining a unique solution!
seed_puzzle = [
    [4, 2, 8, 9, 1, 3, 7, 5, 6],
    [5, 1, 9, 7, 6, 4, 8, 3, 2],
    [7, 6, 3, 2, 8, 5, 1, 9, 4],
    [8, 4, 2, 5, 3, 1, 9, 6, 7],
    [1, 9, 5, 6, 7, 2, 4, 8, 3],
    [6, 3, 7, 8, 4, 9, 5, 2, 1],
    [3, 8, 4, 1, 5, 6, 2, 7, 9],
    [9, 7, 6, 4, 2, 8, 3, 1, 5],
    [2, 5, 1, 3, 9, 7, 6, 4, 8]
]


def random_puzzle(seed=None):
    random.seed(seed)

    # we begin by mutating the puzzle to get a "new" end result

    # first create a LUT to permutate the values
    values = list(range(1, 10))
    random.shuffle(values)
    lut = {i: values[i - 1] for i in range(1, 10)}

    puzzle = [[lut[value] for value in row] for row in seed_puzzle]

    # next we can rotate the puzzle by 0, 90, 180, or 270 degrees
    rotations = random.randint(0, 3)
    for _ in range(rotations):
        puzzle = list(zip(*puzzle[::-1]))

    # then we can flip the puzzle horizontally or vertically (or both)
    if random.randint(0, 1):
        puzzle = [row[::-1] for row in puzzle]
    if random.randint(0, 1):
        puzzle = puzzle[::-1]

    # we can also shuffle box rows/columns
    for _ in range(random.randint(10, 100)):
        shuffle_type = random.randint(0, 1)  # 0 = rows, 1 = cols

        if shuffle_type == 1:
            puzzle = list(zip(*puzzle))

        box_groups = [puzzle[i:i + 3] for i in range(0, 9, 3)]
        random.shuffle(box_groups)
        for box_group in box_groups:
            random.shuffle(box_group)
        puzzle = [line for box_group in box_groups for line in box_group]

        if shuffle_type == 1:
            puzzle = list(zip(*puzzle))

    # we will then begin removing values from the puzzle until no further
    # values can be removed without losing the unique solution

    grid = Grid(puzzle)
    cells = list(grid.get_cells())
    random.shuffle(cells)

    for cell in cells:
        value = cell.value
        cell.reset()
        set_notes(grid)
        if not solve_cell(grid, cell, check=True):
            # if removing the value causes the puzzle to
            # become unsolvable, we must put the value back
            cell.set_value(value)

    for cell in grid.get_cells():
        cell.notes.clear()
        if cell.has_value():
            cell.set_locked(True)

    return grid
