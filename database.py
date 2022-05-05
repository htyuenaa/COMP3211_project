import pickle
import random

from result import Result
from map_vis import plot_map
"""
    file_name for p1 in large map: 'p1_large_db'
    results = [] of result
"""


class Database:
    def __init__(self, agent, map_size, possible_positions=None):
        self.agent = agent
        self.file_name = f'{agent}_{map_size}_db'
        self.results = []
        self.load_and_save()
        self.possible_positions = []
        # only initialize once
        if possible_positions and self.possible_positions == []:
            self.possible_positions = possible_positions

    def __eq__(self, other):
        if type(other) == 'Database':
            return self.file_name == other.file_name
        return False

    def save_to_file(self):
        # save self.results to the file
        print('saving to file...')
        with open(self.file_name, 'wb') as agent_actions_file:
            pickle.dump(self.results, agent_actions_file)
        print(f'saved results to file {self.file_name}!\n')

    def load(self):
        print('loading from file...')
        try:
            with open(self.file_name, 'rb') as saved_actions_for_agent:
                loaded_nodes = pickle.load(saved_actions_for_agent)
            print(f'Searches loaded from {self.file_name}!\n')
            return loaded_nodes
        except FileNotFoundError:
            print('No such file: ' + self.file_name)
            print('creating new file ' + self.file_name + ' ...')
            with open(self.file_name, 'wb') as node_file:
                pickle.dump(self.results, node_file)
            print('creating new file done!\n')
            return []  # returning empty dict for new file

    def load_and_save(self):
        self.results = self.load()

    def add_result(self, new_result):
        if new_result not in self.results:
            self.results.append(new_result)
            print(f'added result {new_result} to the database!')
            return True
        # print(f'result {new_result} already exist in the database!')
        return False

    def get_result(self, init_pos):
        if not self.__contains__(init_pos):
            print(f'result {init_pos} does not exist in the database!')
            return None
        for result in self.results:
            if result.init_pos == init_pos:
                return result.path

    def add_all_results(self, new_results):
        for result in new_results:
            self.add_result(result)

    def sort_results(self, reverse=False):
        self.results.sort(reverse=reverse)
        print('results are sorted in ascending order!')

    def get_random_init_pos(self):
        set1 = set(self.possible_positions)
        set2 = set([r.init_pos for r in self.results])
        set3 = list(set1 - set2)
        if not set3:
            return None
        new_pos = set3[random.randint(0, len(set3) - 1)]
        return new_pos

    def __contains__(self, init_pos: ()):
        r = Result(init_pos)
        return r in self.results

    def add_this_and_other_results(self, result):
        self.add_result(result)
        self.add_all_results(result.get_other_results())

    def dump(self):
        self.results = []

    def add_all_results_from(self, database):
        if self == database:
            self.add_all_results(database.results)

    def plot_travelled_positions(self):
        d = {'p1': 0, 'p2': 1}
        print(f'printing travelled_positions...')
        plot_map([r.init_pos for r in self.results], agent=d[self.agent])


if __name__ == '__main__':
    from utils import *
    db1 = Database(agent='p1', map_size=map_name, possible_positions=possible_positions)
    db1.plot_travelled_positions()
    db2 = Database(agent='p2', map_size=map_name, possible_positions=possible_positions)
    db2.plot_travelled_positions()