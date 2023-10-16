from typing import Optional
import pygame as pygame
from grid import Cell
from solver import set_notes, solve_grid
from generation import random_puzzle

grid = random_puzzle()
surface: pygame.Surface
selected_cell: Optional[Cell] = None

grid_size = 720
grid_margin = 100

cell_size = grid_size / 9
std_font_size = int(cell_size / 2)
std_font: pygame.font.Font

note_size = cell_size / 3
note_font_size = int(std_font_size / 3)
note_font: pygame.font.Font

inst_font_size = int(std_font_size / 2.5)
inst_font: pygame.font.Font


class Colors:
    BLK = (20, 20, 20)
    WHT = (255, 255, 255)
    RED = (234, 52, 52)
    L_RED = (255, 204, 204)
    BLU = (153, 204, 255)
    L_BLU = (219, 237, 255)
    D_BLU = (20, 20, 100)


def initialize_pygame():
    global std_font, note_font, inst_font, surface

    # fonts
    pygame.font.init()
    std_font = pygame.font.SysFont("inter", std_font_size)
    note_font = pygame.font.SysFont("inter", note_font_size)
    inst_font = pygame.font.SysFont("inter", inst_font_size)

    # window (a.k.a. surface)
    pygame.display.set_caption("Sudoku")
    pygame.display.set_mode(
        (grid_size + grid_margin * 2, grid_size + grid_margin * 2))
    surface = pygame.display.get_surface()


def draw():
    surface.fill(Colors.WHT)

    # highlight cells
    for cell in grid.get_cells():
        rect = (
            grid_margin +
            cell_size *
            cell.col,
            grid_margin +
            cell_size *
            cell.row,
            cell_size +
            1,
            cell_size +
            1)
        if cell == selected_cell:
            pygame.draw.rect(surface, Colors.BLU, rect)
        elif not grid.validate_cell(cell):
            pygame.draw.rect(surface, Colors.L_RED, rect)
        elif selected_cell is not None and cell.related_to(selected_cell):
            pygame.draw.rect(surface, Colors.L_BLU, rect)

    # grid lines
    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        offset = grid_margin + cell_size * i
        # vertical
        pygame.draw.line(surface, Colors.BLK, (offset, grid_margin - 1),
                         (offset, grid_margin + grid_size + 1), thickness)
        # horizontal
        pygame.draw.line(surface, Colors.BLK, (grid_margin - 1, offset),
                         (grid_margin + grid_size + 1, offset), thickness)

    # cell values
    for cell in grid.get_cells():
        if cell.has_value():
            color = Colors.BLK if cell.locked else \
                Colors.D_BLU if grid.validate_cell(cell) else Colors.RED
            text = std_font.render(str(cell), True, color)
            text_rect = text.get_rect(
                center=(cell_size / 2, cell_size / 2))
            text_rect = text_rect.move(
                grid_margin + cell_size * cell.col,
                grid_margin + cell_size * cell.row)
            surface.blit(text, text_rect)
        else:
            # if the value isn't set, we draw the notes
            for note in cell.notes:
                text = note_font.render(str(note), True, Colors.BLK)
                text_rect = text.get_rect(
                    center=(note_size / 2, note_size / 2))
                text_rect = text_rect.move(
                    grid_margin + cell_size * cell.col,
                    grid_margin + cell_size * cell.row)
                text_rect = text_rect.move(
                    (note - 1) % 3 * note_size, (note - 1) // 3 * note_size)
                surface.blit(text, text_rect)

    # instructions
    instructions = "Click on a cell to select it, then enter a number. Hit backspace to clear a number. Hold shift to add/remove notes. Use arrow keys to move to adjacent cells. Hit escape or click outside of the grid to deselect a cell. Hit H to get hints for solving the puzzle. Hit enter to auto-solve the puzzle. Hit R to reset the puzzle. Hit C to clear the grid. Hit G to generate a new puzzle.".split()
    lines = []

    while len(instructions) > 0:
        line_words = []
        while len(instructions) > 0:
            line_words.append(instructions.pop(0))
            fw, fh = inst_font.size(' '.join(line_words + instructions[:1]))
            if fw > grid_size:
                break
        lines.append(' '.join(line_words))

    for i, line in enumerate(lines):
        text = inst_font.render(line, True, Colors.BLK)
        surface.blit(text, (grid_margin, grid_margin +
                     grid_size + inst_font_size * (i + 1)))


def process_events():
    global grid
    redraw = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # cell selection
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if grid_margin <= x <= grid_margin + \
                    grid_size and grid_margin <= y <= grid_margin + grid_size:
                row = int((y - grid_margin) / cell_size)
                col = int((x - grid_margin) / cell_size)
                global selected_cell
                selected_cell = grid.get_cell(row, col)
            else:
                selected_cell = None

            redraw = True
            continue

        if event.type != pygame.KEYDOWN:
            continue

        if selected_cell is not None:
            if event.key == pygame.K_ESCAPE:
                selected_cell = None
                redraw = True
                continue

            direction = None

            if event.key == pygame.K_LEFT:
                direction = (0, -1)
            elif event.key == pygame.K_RIGHT:
                direction = (0, 1)
            elif event.key == pygame.K_UP:
                direction = (-1, 0)
            elif event.key == pygame.K_DOWN:
                direction = (1, 0)

            if direction is not None:
                new_row = (selected_cell.row + direction[0]) % 9
                new_col = (selected_cell.col + direction[1]) % 9
                selected_cell = grid.get_cell(new_row, new_col)
                redraw = True
                continue

        # number input
            if pygame.K_0 < event.key <= pygame.K_9:
                digit = event.key - pygame.K_0
                # use shift modifier for notes
                if event.mod & pygame.KMOD_SHIFT:
                    if digit in selected_cell.notes:
                        selected_cell.notes.remove(digit)
                    else:
                        selected_cell.notes.append(digit)
                else:
                    selected_cell.set_value(digit)
                    for cell in grid.get_related_cells(selected_cell):
                        if digit in cell.notes:
                            cell.notes.remove(digit)
                redraw = True
                continue
            elif event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
                selected_cell.reset()
                redraw = True
                continue

        # clearing
        if event.key == pygame.K_r:
            for cell in grid.get_cells():
                cell.reset()
            redraw = True
        elif event.key == pygame.K_c:
            for cell in grid.get_cells():
                cell.set_locked(False)
                cell.reset()
            redraw = True
        # regenerating
        elif event.key == pygame.K_g:
            grid = random_puzzle()
            redraw = True
        # solving
        elif event.key == pygame.K_RETURN:
            solve_grid(grid)
            redraw = True
        elif event.key == pygame.K_h:
            set_notes(grid)
            redraw = True
        # dump to string
        elif event.key == pygame.K_p:
            print(str(grid))

    if redraw:
        draw()

    return True


def launch():
    initialize_pygame()
    draw()
    while True:
        if process_events():
            pygame.display.update()
        else:
            break


if __name__ == "__main__":
    launch()
