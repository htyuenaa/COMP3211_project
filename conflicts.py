"""
@argtype: Result, Result
@rtype: Condition
"""
from result import Result
from datetime import datetime


def find_first_collision(results):
    result1, result2 = results['p1'].get_copy(), results['p2'].get_copy()
    if result1 < result2:
        result1.padding(result2.get_cost())
    elif result2 < result1:
        result2.padding(result1.get_cost())
    # print(result1.path)
    # print(result2.path)
    # has_collision = lambda x, y, t: False if x != y else t
    # collision = [has_collision(x, y, t) for x, y, t in
    #              zip(result1.path, result2.path, [z + 1 for z in range(result1.get_cost())])]
    # collision = tuple(filter(lambda x: x is not False, collision))
    merged = [(x, y) for x, y in zip(result1.path, result2.path)]
    for i in range(len(merged) - 1):
        if merged[i][0] == merged[i][1] or \
                (merged[i + 1][0] == merged[i][1] and merged[i][0] == merged[i + 1][1]):
            return i+1


# @rtype: (x, y), time, (x, y), time
# for p1 and p2
def generate_conditions(results, colliding_time):
    result1, result2 = results['p1'], results['p2']
    c1, c2 = None, None
    if colliding_time <= result1.get_cost():
        c1 = Condition(result1.path[colliding_time - 1], colliding_time)
    if colliding_time <= result2.get_cost():
        c2 = Condition(result2.path[colliding_time - 1], colliding_time)
    return c1, c2


class Condition:
    def __init__(self, collision_pos, time):
        self.position = collision_pos
        self.time = time

    def __repr__(self):
        return f'{self.position}, {self.time}'


if __name__ == '__main__':
    from database import Database
    from utils import *

    # db1 = Database(agent='p1', map_size=map_name)
    # db2 = Database(agent='p2', map_size=map_name)
    # result1 = Result((1, 1), [(1, 2), (1, 3), (2, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)])
    # result2 = Result((5, 1), [(5, 2), (5, 3), (4, 3), (3, 3)])
    # results = {'p1': result1, 'p2': result2}
    # collision = find_first_collision(results)
    # condition = generate_conditions(results, collision)
    # print(condition)
    #
    # result2 = Result((5, 1), [(5, 2), (5, 3), (4, 3), (5, 3)])
    # results = {'p1': result1, 'p2': result2}
    # collision = find_first_collision(results)
    # # condition = generate_conditions(results, collision)
    # # print(condition)
    # print()
    #
    # result1 = Result((1, 1), [(1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)])
    # result2 = Result((5, 1), [(5, 2), (5, 3), (4, 3), (3, 3)])
    # results = {'p1': result1, 'p2': result2}
    # collision = find_first_collision(results)
    # condition = generate_conditions(results, collision)
    # print(condition)
    #
    # print(results)
    # print(results['p1'].path)
    # print(results['p2'].path)
    from node import Node
    current_node = Node()