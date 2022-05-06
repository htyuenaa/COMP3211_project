from base import action_dict, move


# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position: (), parent: (), end: ()):
        self.position = position
        self.parent = parent
        dist = lambda n1, n2: abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
        if parent is None:  # root node
            self.g = 0
        else:
            self.g = parent.g + 1
        self.h = dist(self.position, end)
        self.f = self.g + self.h
        # Generate heuristics (Manhattan distance)

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return '({0},{1})'.format(self.position, self.f)

    # define hash
    def __hash__(self):
        return hash(self.position)

    # all neighbors returned must be valid
    def get_neighbors(self, layout, having_condition=False):
        neighbors = []
        map_size = len(layout)
        for action in action_dict:
            # the search don't have any conditions, skip the nil action
            if action == 'nil' and not having_condition:
                continue
            (new_y, new_x) = move(self.position, action)
            # if out map/ not valid move -> not appending
            if 0 <= new_y < map_size and 0 <= new_x < map_size:
                if layout[new_y][new_x] == 0:
                    neighbors.append((new_y, new_x))
        return neighbors

    def is_goal(self, goal_node):
        return self == goal_node

    def violate(self, conditions=None):
        if not conditions:
            return False
        for condition in conditions:
            # print(f'condition: {condition}, node pos, g: {self.position}, {self.g}')
            # print(f'position are same: {self.position == condition.position}')
            # print(f'time are same: {self.g == condition.time}')
            if self.position == condition.position and self.g == condition.time:
                # print('violation detected')
                return True
        return False
