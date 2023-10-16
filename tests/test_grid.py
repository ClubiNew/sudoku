import unittest
from grid import Grid
from examples import solvable, remainder_grid, remainder_validation, remainder_string

# TODO: test cell locking, has_value, set_value, reset, related_to, get_cells, get_related_cells


class CellValidationTests(unittest.TestCase):
    def test_empty_grid(self):
        grid = Grid()
        for cell in grid.get_cells():
            self.assertTrue(grid.validate_cell(cell))

    def test_invalid_grid(self):
        grid = Grid([[1 for col in range(9)] for row in range(9)])
        for cell in grid.get_cells():
            self.assertFalse(grid.validate_cell(cell))

    def test_remainder_grid(self):
        grid = Grid(remainder_grid)
        for cell in grid.get_cells():
            self.assertEqual(grid.validate_cell(
                cell), remainder_validation[cell.row][cell.col])


class GridSolvedTests(unittest.TestCase):
    def test_empty_grid(self):
        empty_grid = Grid()
        self.assertFalse(empty_grid.is_solved())

    def test_invalid_grid(self):
        invalid_grid = Grid(remainder_grid)
        self.assertFalse(invalid_grid.is_solved())

    def test_solvable_grids(self):
        for example in solvable:
            unsolved = Grid(example["unsolved"])
            self.assertFalse(unsolved.is_solved())
            solved = Grid(example["solved"])
            self.assertTrue(solved.is_solved())


class ConversionTests(unittest.TestCase):
    def test_from_array(self):
        grid = Grid(remainder_grid)
        for row in range(9):
            for col in range(9):
                cell_value = grid.get_cell(row, col).value
                self.assertEqual(cell_value, (row + col) % 9 + 1)

    def test_to_array(self):
        grid = Grid([[(row + col) % 9 + 1 for col in range(9)]
                    for row in range(9)])
        for index, row in enumerate(grid.to_array()):
            self.assertListEqual(row, remainder_grid[index])

    def test_to_str(self):
        grid = Grid(remainder_grid)
        self.assertEqual(str(grid), remainder_string)


if __name__ == "__main__":
    unittest.main()
