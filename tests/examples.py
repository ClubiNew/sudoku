remainder_grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

remainder_string = """[
\t[1, 2, 3, 4, 5, 6, 7, 8, 9],
\t[2, 3, 4, 5, 6, 7, 8, 9, 1],
\t[3, 4, 5, 6, 7, 8, 9, 1, 2],
\t[4, 5, 6, 7, 8, 9, 1, 2, 3],
\t[5, 6, 7, 8, 9, 1, 2, 3, 4],
\t[6, 7, 8, 9, 1, 2, 3, 4, 5],
\t[7, 8, 9, 1, 2, 3, 4, 5, 6],
\t[8, 9, 1, 2, 3, 4, 5, 6, 7],
\t[9, 1, 2, 3, 4, 5, 6, 7, 8]
]"""

remainder_validation = [
    [True, False, False, True, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, True, False, False, True],
    [True, False, False, True, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, True, False, False, True],
    [True, False, False, True, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, True, False, False, True],
]
