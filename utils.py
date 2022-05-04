from run import parse_map_from_file

# Initiating the environment
goals = {'small': {'p1': (5, 5), 'p2': (3, 3)},
         'medium': {'p1': (9, 7), 'p2': (5, 9)},
         'large': {'p1': (150, 125), 'p2': (100, 175)}}

map_name, agent = 'large', 'p1'
layout = parse_map_from_file(map_name)
goal = goals[map_name][agent]
map_size = len(layout)

possible_positions = []
for y in range(map_size):
    for x in range(map_size):
        if layout[y][x] == 0:
            if not (165 <= y <= 202 and 0 <= x <= 40) and not (y > 250 and 20 < x <= 53):
                possible_positions.append((y, x))
