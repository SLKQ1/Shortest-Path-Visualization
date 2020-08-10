import pygame
import math
import PathFindingAlgorithms.aStar as aStar
from PathFindingAlgorithms.bfs import bfs
# window settings
pygame.init()
mainClock = pygame.time.Clock()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Shortest Path Algorithm Visualization")
# colors being used
PATH_GREEN = (62, 242, 2)
START_GREEN = (0, 166, 69)
BLUE_DARK = (30, 115, 252)
BLUE_LIGHT = (120, 170, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 47, 5)


# node class to represent all nodes on grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        # coordinate position of node
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []

    # function to get position
    def get_position(self):
        return self.row, self.col

    # method to see if node is closed
    def is_closed(self):
        return self.color == BLUE_DARK

    # method to see if node is open
    def is_open(self):
        return self.color == BLUE_LIGHT

    # method to see if node is a barrier
    def is_barrier(self):
        return self.color == BLACK

    # method to see if node is start node
    def is_start(self):
        return self.color == START_GREEN

    # method to see if node is end node
    def is_end(self):
        return self.color == RED

    # method to reset the color
    def reset(self):
        self.color = WHITE

    # method to open node
    def make_open(self):
        self.color = BLUE_LIGHT

    # method to close a node
    def make_closed(self):
        self.color = BLUE_DARK

    # method to make node into barrier
    def make_barrier(self):
        self.color = BLACK

    # method to make node into end node
    def make_end(self):
        self.color = RED

    # method to make node into start node
    def make_start(self):
        self.color = START_GREEN

    # method to make node into path node
    def make_path(self):
        self.color = PATH_GREEN

    # method to draw node
    def draw(self, WIN):
        pygame.draw.rect(
            WIN, self.color, (self.x, self.y, self.width, self.width))

    # method to update neighbors
    def update_neighbors(self, grid):
        self.neighbors = []
        # checking if up neighbor is a barrier
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        # checking if down neighbor is a barrier
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        # checking if left neighbor is a barrier
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        # checking if right neighbor is a barrier
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

    # method to handle comparison between two nodes
    def __lt__(self, other):
        return False


# function to make grid
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
                    # aStar.a_Star(lambda: draw(
                    #     WIN, grid, ROWS, width), grid, start, end)

                    # BFS
                    bfs(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
    pygame.quit()
    sys.exit()


main(WIN, WIDTH)
