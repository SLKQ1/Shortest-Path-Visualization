import pygame
# importing colors
from components.colors import *


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
