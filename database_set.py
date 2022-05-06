from database import Database, pickle, Result


class Dataset(Database):
    def __init__(self, agent, map_size, possible_positions=None):
        super().__init__(agent, map_size, possible_positions)
        if type(self.results) == list:
            self.results = set(self.results)

    def __repr__(self):
        num_of_results = len(self.results)
        total_num = len(self.possible_positions)
        rate = round(num_of_results / total_num, 3) * 100
        return f'agent: {self.agent}, file name: {self.file_name}\n' \
               f'Number of results: {num_of_results}\n' \
               f'Total number of results: {total_num}\n' \
               f'Rate of completion: {rate}%\n'

    def add_all_results(self, new_results_set):
        self.results.update(new_results_set)

    def get_result(self, init_pos: ()):
        iterator = iter(self.results)
        result = None
        while result is None:
            next_item = next(iterator, None)
            if next_item.init_pos == init_pos:
                result = next_item
        return result

    # new result is a set
    def add_result(self, new_result):
        self.results.add(new_result)
        print(f'added result {new_result} to the database!')

    def add_this_and_other_results(self, result):
        self.results.add(result)
        other_results = result.get_other_results()
        self.results.update(other_results)
        print(f'added other results {other_results} to the database!')

    def __contains__(self, init_pos):
        return Result(init_pos) in self.results


if __name__ == '__main__':
    from utils import possible_positions
    ds1 = Dataset(agent='p1', map_size='large', possible_positions=possible_positions)
    ds2 = Dataset(agent='p2', map_size='large', possible_positions=possible_positions)
    # ds1.save_to_file()

