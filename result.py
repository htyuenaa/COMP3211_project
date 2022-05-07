import copy


class Result:
    def __init__(self, init_pos, path=[]):
        self.init_pos = init_pos
        self.path = path

    def get_other_results(self):
        results = set()
        for i in range(len(self.path) - 1):
            results.add(Result(self.path[i], self.path[i:]))
        return results

    def __repr__(self):
        return f'{self.init_pos}'

    def __eq__(self, other):
        return self.init_pos == other.init_pos

    def __lt__(self, other):
        return self.get_cost() < other.get_cost()

    def get_cost(self):
        return len(self.path)

    def print(self):
        print(f'init_pos: {self.init_pos}, path: {self.path}')

    def __hash__(self):
        return hash(self.init_pos)

    def padding(self, time):
        last_position = self.path[-1] if len(self.path)>0 else self.init_pos
        while self.get_cost() < time:
            self.path.append(last_position)

    # clone this object
    def get_copy(self):
        return copy.deepcopy(self)
