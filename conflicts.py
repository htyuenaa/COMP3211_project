class Conflict:
    def __init__(self, result1, result2):
        self.result1 = result1
        self.result2 = result2
        self.conflict = self.find_first_collision(result1, result2)

    def find__first_collision(self, r1, r2):
        cost1 = r1.get_cost()
        cost2 = r2.get_cost()
        for i in range(max(cost1, cost2)-1):
            try:
                pos1 = r1.path[i]
            except IndexError:
                pos1 = r1.path[-1]
            try:
                pos2 = r1.path[i]
            except IndexError:
                pos2 = r1.path[-1]
            if pos1 == pos2:
                return i+1
        return None

    def resolve_conflicts(self, path1, path2):
        pass

    def insert_nil(self, path):
        pass


if __name__ == '__main__':
    from database import Database
    from utils import *
    db = Database(agent=agent, map_size=map_name, possible_positions=possible_positions)
    r1 = db.get_result((1, 1))
    r2 = db.get_result((1, 2))
    conflict = Conflict(r1, r2)
