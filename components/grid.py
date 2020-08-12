from components.node import Node
import pygame
# importing colors
from components.colors import (GREY, WHITE)


def make_grid(rows, width):
    grid = []
    node_width = width // rows

    for row in range(rows):
        grid.append([])
        for col in range(rows):
            node = Node(row, col, node_width, rows)
            grid[row].append(node)

    return grid

# function to draw grid lines


def draw_grid_lines(WIN, rows, width):
    node_width = width // rows

    for x in range(rows):
        pygame.draw.line(WIN, GREY, (0, x * node_width),
                         (width, x * node_width))
        for y in range(rows):
            pygame.draw.line(WIN, GREY, (y * node_width, 0),
                             (y * node_width, width))


# function to draw and redraw grid
def draw(WIN, grid, rows, width):
    WIN.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(WIN)

    draw_grid_lines(WIN, rows, width)
    pygame.display.update()
