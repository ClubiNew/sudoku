from grid import Grid, Cell, Relation


def set_notes(grid: Grid):
    for cell in grid.get_cells():
        if cell.has_value():
            continue

        notes = list(range(1, 10))

        for other_cell in grid.get_related_cells(cell):
            if other_cell.value in notes:
                notes.remove(other_cell.value)

        cell.notes = notes


def solve_cell(grid: Grid, cell: Cell, check: bool = False):
    # if a cell has only one possible value, it must be that value
    if len(cell.notes) == 1:
        if not check:
            cell.set_value(cell.notes[0])
        return True

    # if a note is only possible in one cell in a relation, it must be in
    # that cell
    for relation in [Relation.ROW, Relation.COL, Relation.BOX]:
        unique_notes = cell.notes.copy()

        for other_cell in grid.get_related_cells(cell, relation):
            for note in other_cell.notes:
                if note in unique_notes:
                    unique_notes.remove(note)

        if len(unique_notes) == 1:
            if not check:
                cell.set_value(unique_notes[0])
            return True

    return False


def solve_grid(grid: Grid):
    changed = True
    while changed:
        set_notes(grid)
        changed = False
        for cell in grid.get_cells():
            if cell.has_value():
                continue
            if solve_cell(grid, cell):
                changed = True
                break

    return grid
