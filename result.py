class Result:
    def __init__(self, init_pos, path=[]):
        self.init_pos = init_pos
        self.path = path

    def get_other_results(self):
        results = []
        for i in range(len(self.path)-1):
            results.append(Result(self.path[i], self.path[i:]))
        return results

    def __repr__(self):
        return f'{self.init_pos}'

    def __eq__(self, other):
        return self.init_pos == other.init_pos

    def __lt__(self, other):
        return self.init_pos[0] < other.init_pos[0] if \
            self.init_pos[0] != other.init_pos[0] else self.init_pos[1] < other.init_pos[1]

    def get_cost(self):
        return len(self.path)

    def print(self):
        print(f'init_pos: {self.init_pos}, path: {self.path}')
