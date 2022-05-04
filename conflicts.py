class Conflict:
    def __init__(self, result1, result2):
        self.result1 = result1
        self.result2 = result2
        self.conflict = self.find_collision(result1, result2)

    def find_collision(self, r1, r2):

        return None

    def resolve_conflicts(self, path1, path2):
        pass

    def insert_nil(self, path):
        pass
