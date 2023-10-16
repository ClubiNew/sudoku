from __future__ import annotations


class Relation():
    ROW = 0b001
    COL = 0b010
    BOX = 0b100
    ALL = 0b111


class Cell:
    notes: list[int]

    def __init__(self, row: int, col: int, value: int = 0):
        self.row = row
        self.col = col
        self.value = value
        self.notes = []

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def has_value(self):
        return self.value != 0

    def set_value(self, value: int):
        self.value = value
        self.notes.clear()

    def reset(self):
        self.value = 0
        self.notes.clear()

    def related_to(self, cell: Cell, relation: Relation = Relation.ALL):
        if cell == self:
            return False
        same_row = (relation & Relation.ROW) and self.row == cell.row
        same_col = (relation & Relation.COL) and self.col == cell.col
        same_box = (relation & Relation.BOX) and \
            self.row // 3 == cell.row // 3 and self.col // 3 == cell.col // 3
        return same_row or same_col or same_box


class Grid:
    def __init__(self, values: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]):
        self.rows = [[Cell(r, c, values[r][c])
                      for c in range(9)] for r in range(9)]

    def __str__(self):
        rows = [', '.join([str(self.rows[row][col])
                          for col in range(9)]) for row in range(9)]
        return f"[\n\t[{'],\n\t['.join(rows)}]\n]"

    def to_array(self):
        return [[int(self.rows[row][col]) for col in range(9)] for row in range(9)]

    def get_cell(self, row: int, col: int) -> Cell:
        return self.rows[row][col]

    def get_cells(self):
        return (cell for row in self.rows for cell in row)

    def get_related_cells(self, cell: Cell, relation: Relation = Relation.ALL):
        return (other_cell for other_cell in self.get_cells() if cell.related_to(other_cell, relation))

    def validate_cell(self, cell: Cell):
        if not cell.has_value():
            return True

        for other_cell in self.get_related_cells(cell):
            if other_cell != cell and other_cell.value == cell.value:
                return False

        return True
