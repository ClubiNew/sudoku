import unittest
from grid import Grid
from solver import solve_grid
from examples import solvable


class SolverTests(unittest.TestCase):
    def test_solvable_grids(self):
        for example in solvable:
            grid = Grid(example["unsolved"])
            solved = solve_grid(grid).to_array()
            for solved_row, golden_row in zip(solved, example["solved"]):
                self.assertListEqual(solved_row, golden_row)

    def test_empty_grid(self):
        grid = solve_grid(Grid())
        for cell in grid.get_cells():
            self.assertListEqual(cell.notes, list(range(1, 10)))


if __name__ == "__main__":
    unittest.main()
