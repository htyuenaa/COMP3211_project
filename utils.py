from run import parse_map_from_file

# Initiating the environment
goals = {'small': {'p1': (5, 5), 'p2': (3, 3)},
         'medium': {'p1': (9, 7), 'p2': (5, 9)},
         'large': {'p1': (150, 125), 'p2': (100, 175)}}

map_name = 'large'
layout = parse_map_from_file(map_name)
map_size = len(layout)

possible_positions = []
boundary_positions = []
for y in range(map_size):
    for x in range(map_size):
        if layout[y][x] == 0:
            if not (y > 110 and x < 75):
                # valid positions
                possible_positions.append((y, x))


def get_agent():
    agent = input('agent: ')
    if agent not in ['p1', 'p2']:
        print('agent not found')
        return get_agent()
    return agent


corners = [(0, 0), (1, 125), (0, 255),
           (125, 0), (125, 125), (125, 225),
           (255, 0), (255, 125), (255, 255)]
