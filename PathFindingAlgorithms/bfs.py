import pygame
from queue import Queue


def bfs(draw, grid, start, end):
    # initialize q and add starting node
    queue = Queue()
    queue.put(start)

    # make a visited array of none and setting starting node to visited
    visited = {node: False for row in grid for node in row}
    visited[start] = True

    # making an array of prev
    prev = {node: None for row in grid for node in row}

    while not queue.empty():
        # allowing the user to exit while algorithm is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # getting the current node
        node = queue.get()
        # if the end is reached
        if node == end:
            reconstruct_path(prev, node, draw)
            start.make_start()
            return True

        # considering all neighbors of current node
        for neighbor in node.neighbors:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
                prev[neighbor] = node
                if neighbor != end:
                    neighbor.make_open()
        draw()
        # closing current node after consideration, if its not the start node
        if node != start:
            node.make_closed()
    # return prev
    return False


def reconstruct_path(prev, current, draw):
    while current in prev:
        current = prev[current]
        if current != None:
            current.make_path()
        draw()
