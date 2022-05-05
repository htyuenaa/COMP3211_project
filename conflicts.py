"""
@rtype: collision time, collision position
"""
def find_first_collision(p1, p2):
    cost1, cost2 = len(p1), len(p2)
    for i in range(max(cost1, cost2) - 1):
        try:
            pos1 = p1[i]
        except IndexError:
            pos1 = p1[-1]
        try:
            pos2 = p2[i]
        except IndexError:
            pos2 = p2[-1]
        if pos1 == pos2:
            return i + 1, pos1
    return None, None


class Conflict:
    def __init__(self, result1, result2):
        self.path1 = result1.path
        self.path2 = result2.path
        self.conflict, self.conflict_time = find_first_collision(self.path1, self.path2)

    def resolve_conflicts(self, path1, path2):
        if self.conflict is None:
            return True

    def insert_nil_action(self, path):
        pass


if __name__ == '__main__':
    from database import Database
    from utils import *

    db1 = Database(agent='p1', map_size=map_name)
    db2 = Database(agent='p2', map_size=map_name)
    r1 = db1.get_result((1, 1))
    r2 = db2.get_result((1, 2))
    conflict = Conflict(r1, r2)
