import unittest
from grid import Grid
from solver import solve
from examples import solvable


class SolverTests(unittest.TestCase):
    def test_solvable_grids(self):
        for example in solvable:
            grid = Grid(example["unsolved"])
            for solved_row, golden_row in zip(
                    solve(grid).to_array(), example["solved"]):
                self.assertListEqual(solved_row, golden_row)

    def test_empty_grid(self):
        grid = solve(Grid())
        for cell in grid.get_cells():
            self.assertListEqual(cell.notes, list(range(1, 10)))


if __name__ == "__main__":
    unittest.main()
