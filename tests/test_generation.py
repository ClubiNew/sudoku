import unittest
from generation import random_puzzle
from solver import solve_grid
from examples import seeded


class GeneratorTests(unittest.TestCase):
    def test_seeds(self):
        for example in seeded:
            grid = random_puzzle(example["seed"])
            for row, golden in zip(grid.to_array(), example["output"]):
                self.assertListEqual(row, golden)

    def test_solvable(self):
        for seed in range(-10000, 10000, 1000):
            grid = random_puzzle(seed)
            self.assertTrue(solve_grid(grid).is_solved())

    def test_uniqueness(self):
        for seed in range(-10000, 10000, 1000):
            grid_1 = random_puzzle(seed)
            grid_2 = random_puzzle(seed + 1)
            for row_1, row_2 in zip(grid_1.to_array(), grid_2.to_array()):
                self.assertNotEqual(row_1, row_2)


if __name__ == "__main__":
    unittest.main()
