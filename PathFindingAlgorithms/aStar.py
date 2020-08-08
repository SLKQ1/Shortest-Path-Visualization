import pygame
from queue import PriorityQueue


# function to reconstruct path
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


# heuristic funcition for A* (Manhatten Distance)
def heuristic(n1, n2):
    x1, y1 = n1
    x2, y2 = n2

    return abs(x1 - x2) + abs(y1 - y2)


# function for A* algorithm
def a_Star(draw, grid, start, end):
    # count var to see which node was inserted first (in order to break ties)
    count = 0
    # open set to store nodes that we are currently considering
    open_set = PriorityQueue()

    # adding start node to open set (f-score, count, node)
    open_set.put((0, count, start))
    # dictionary to store what node we came from
    came_from = {}

    # setting all g-scores to be infinite
    g_score = {node: float("inf") for row in grid for node in row}
    # setting g-score for start node to be 0
    g_score[start] = 0

    # setting all f-scores to be infinite
    f_score = {node: float("inf") for row in grid for node in row}
    # setting f-score for start node to be h-score
    f_score[start] = heuristic(start.get_position(), end.get_position())

    # dictionary to keep track of what elements are in the priority queue
    open_set_hash = {start}

    while not open_set.empty():
        # allowing the user to exit while algorithm is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # removing the current node from priority queue and hash
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # if the current node is the end node, shortest path found
        if current == end:
            reconstruct_path(came_from, current, draw)
            start.make_start()
            return True

        # considering all neighbors of current node
        for neighbor in current.neighbors:
            temp_g_score_of_neighbor = g_score[current] + 1

            # if the temp is less then the current g-score of the neighbor then update in open set
            if temp_g_score_of_neighbor < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score_of_neighbor
                f_score[neighbor] = temp_g_score_of_neighbor + \
                    heuristic(neighbor.get_position(), end.get_position())

                # adding neighbor to open set
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    # opening neighbor
                    if neighbor != end:
                        neighbor.make_open()

        draw()
        # closing current node after consideration, if its not the start node
        if current != start:
            current.make_closed()

    # if no path found
    return False
