import pygame

# importing algorithms
from PathFindingAlgorithms.aStar import aStar
from PathFindingAlgorithms.bfs import bfs
from PathFindingAlgorithms.dfs import dfs
from PathFindingAlgorithms.dijkstra import dijkstra, reconstruct_path

# importing node class
from components.node import Node

# importing grid
from components.grid import *

# setting up pygame
pygame.init()
mainClock = pygame.time.Clock()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Shortest Path Algorithm Visualization")


# function to locate mouse click position
def get_clicked_position(position, rows, width):
    row_width = width // rows
    x, y = position

    row = x // row_width
    col = y // row_width

    return row, col


# main function
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    # starting and ending positions on init
    start = None
    end = None

    # program running
    run = True
    while run:
        draw(WIN, grid, ROWS, width)
        # checking all game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            # checking if left mouse button pressed
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, ROWS, width)
                node = grid[row][col]

                # if start is none make it
                if not start and node != end:
                    start = node
                    start.make_start()

                # if end is none make it
                elif not end and node != start:
                    end = node
                    end.make_end()

                # if the node is not the start or end make it a barrier
                elif node != start and node != end:
                    node.make_barrier()

            # checking if right mouse button was pressed
            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, ROWS, width)
                node = grid[row][col]
                # erasing the node (turn white)
                node.reset()
                # set the start and end to none if those were erased
                if node == start:
                    start = None
                elif node == end:
                    end = None

            # run algorithm when space is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    # A*
                    aStar(lambda: draw(
                        WIN, grid, ROWS, width), grid, start, end)

                    # BFS
                    # bfs(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main(WIN, WIDTH)
