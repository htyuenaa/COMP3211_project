import numpy as np
from node import Node


def a_star_search(layout=np.array, start=(), end=(), database=None):
    # Create a start node and an goal node
    start_node = Node(start, None, end)
    goal_node = Node(end, None, end)
    # Create sets for open nodes and closed nodes
    open = []  # open: queue for nodes waiting to be expanded
    closed = set()  # closed: set for nodes expanded (we don't care the orders)
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        if current_node not in closed:
            closed.add(current_node)
        # only print 100 nodes to avoid flooding the console
        # print(f'open {open[:100]}')
        # print(f'closed {closed[-100:]}\n')

        # check if we passed in the database
        # check if current node is travelled before
        current_pos = current_node.position
        if database.__contains__(current_pos):
            result = database.get_result(current_pos)
            if result.get_cost() == current_node.h:
                # we can use the previous searching result
                path = []
                while current_node != start_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                # Return reversed path
                return path[::-1] + result.path

        # Check if we have reached the goal, return the path
        if current_node.is_goal(goal_node):
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            # Return reversed path
            return path[::-1]
        # Get neighbors
        neighbors = current_node.get_neighbors(layout)

        # Loop neighbors
        for next_node in neighbors:
            neighbor = Node(next_node, current_node, end)
            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open, neighbor):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


# Check if a neighbor should be added to open list
# only add this neighbor if:
# new node or take few steps than before
def add_to_open(open, neighbor):
    if neighbor not in open:
        return True
    node = tuple(filter(lambda x: neighbor.f < x.f and x == neighbor, open))
    if node:
        # if the neighbor should be added to the list
        # remove the original one with higher cost
        open.remove(node[0])
        return True
    return False


# conditions: set of Condition objects
def a_star_search_with_conditions(layout=np.array, start=(), end=(), database=None, conditions=None):
    if start == end:
        return [start]
    # Create a start node and a goal node
    start_node = Node(start, None, end)
    goal_node = Node(end, None, end)
    # Create sets for open nodes and closed nodes
    open = []  # open: queue for nodes waiting to be expanded
    closed = set()  # closed: set for nodes expanded (we don't care the orders)
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()

        # only print 100 nodes to avoid flooding the console
        # print(f'open {open[:100]}')
        # print(f'closed {closed[-100:]}\n')

        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        if current_node not in closed:
            closed.add(current_node)

        if database:
            # check if current node is travelled before
            current_pos = current_node.position
            if database.__contains__(current_pos):
                result = database.get_result(current_pos)
                if result.get_cost() == current_node.h and not current_node.violate(conditions):
                    # we can use the previous searching result
                    path = [current_node.position]
                    current_node = current_node.parent
                    while current_node.parent is not None:
                        path.append(current_node.position)
                        current_node = current_node.parent
                    # Return reversed path
                    return path[::-1] + result.path

        # Check if we have reached the goal, return the path
        if current_node.is_goal(goal_node) and not current_node.violate(conditions):
            path = [current_node.position]
            current_node = current_node.parent
            while current_node.parent is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            # Return reversed path
            return path[::-1]

        # Get neighbors
        have_collisions = conditions is not None
        neighbors = current_node.get_neighbors(layout, have_collisions)

        # Loop neighbors
        for next_node in neighbors:
            neighbor = Node(next_node, current_node, end)
            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open_with_conditions(open, neighbor, conditions):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


def add_to_open_with_conditions(open, neighbor, conditions):
    if neighbor.violate(conditions):
        return False
    if neighbor not in open:
        return True
    node = tuple(filter(lambda x: neighbor.f < x.f and x == neighbor, open))
    if node:
        # if the neighbor should be added to the list
        # remove the original one with higher cost
        open.remove(node[0])
        return True
    return False
