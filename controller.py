import copy

from search import a_star_search_with_conditions, a_star_search
from conflicts import *

"""
    Example of input args
    map_size = 'small'
    layout: n * n np.array
    starts: {'p1': (1, 1), 'p2': (5, 1)}
    goals: {'p1': (5, 5), 'p2': (3, 3)}
"""


class State:
    agents_name = ['p1', 'p2']

    def __init__(self, init_pos, goal, conditions=None, parent_state=None):
        self.initial_positions = init_pos
        self.goals = goal
        self.conditions = {'p1': set(), 'p2': set()}
        if conditions is not None:
            self.conditions = copy.deepcopy(conditions)
        self.results = {'p1': Result(init_pos['p1']), 'p2': Result(init_pos['p2'])}
        self.cost = {'p1': 0, 'p2': 0}
        self.parent = parent_state

    def __repr__(self):
        return f'init_pos:{self.initial_positions} goal:{self.goals}\n' \
               f'conditions: {self.conditions}\n' \
               f'results:\n' \
               f"p1: {self.results['p1'].path}\n" \
               f"p2: {self.results['p2'].path}"

    def run_search(self, layout):
        # can soon modify it to do in parallel
        if self.conditions['p1'] == set() and self.conditions['p2'] == set():
            for name in State.agents_name:
                path = a_star_search(layout, self.initial_positions[name], self.goals[name])
                self.results[name] = Result(self.initial_positions[name], path)
                self.cost[name] = self.results[name].get_cost()
        else:
            for name in State.agents_name:
                if self.conditions[name] == self.parent.conditions[name]:
                    self.results[name] = copy.deepcopy(self.parent.results[name])
                    self.cost[name] = self.results[name].get_cost()
                else:
                    path = a_star_search_with_conditions(layout, self.initial_positions[name], self.goals[name], conditions=self.conditions[name])
                    self.results[name] = Result(self.initial_positions[name], path)
                    self.cost[name] = self.results[name].get_cost()

    def get_total_cost(self):
        return self.cost['p1']+self.cost['p2']

    def __hash__(self):
        condition = tuple(
            (tuple(self.conditions['p1']),
             tuple(self.conditions['p2']))
        )
        return hash(condition)

    def __eq__(self, other_state):
        return self.conditions == other_state.conditions

    def __lt__(self, other_state):
        return self.get_total_cost() < other_state.get_total_cost()

    # return new states with conditions
    def get_new_states(self, condition1, condition2):
        state1 = State(self.initial_positions, self.goals, self.conditions, parent_state=self)
        if condition1 and condition1 not in state1.conditions['p1']:
            state1.conditions['p1'].add(condition1)
            state1.results['p1'] = self.results['p1']
        state2 = State(self.initial_positions, self.goals, self.conditions, parent_state=self)
        if condition2 and condition2 not in state2.conditions['p2']:
            state2.conditions['p2'].add(condition2)
            state1.results['p2'] = self.results['p2']
        return [state1, state2]


class Controller:
    def __init__(self, layout, starts, goals):
        self.layout = layout
        self.init_state = State(starts, goals)
        self.solution_state = None

    def find_solution(self):
        state = self.init_state
        queue = []
        close = set()
        queue.append(state)
        count = 0
        while True and count < 5:
            # count += 1
            # print(f'count: {count}')
            # print('queue: ')
            # for node in queue:
            #     print(node)

            current_best_state = queue.pop(0)
            current_best_state.run_search(self.layout)
            if current_best_state not in close:
                close.add(current_best_state)
            print('printing current best state...')
            print(current_best_state)
            collision = find_first_collision(current_best_state.results)
            if find_first_collision(current_best_state.results) is None:
                # finish and return
                self.solution_state = current_best_state
                return
            condition1, condition2 = generate_conditions(current_best_state.results, collision)
            new_states = current_best_state.get_new_states(condition1, condition2)
            for state in new_states:
                # print('new state: ')
                # print(state)
                if state not in queue and state is not None:
                    queue.append(state)

    def get_solution(self):
        if not self.solution_state:
            return None
        return {'p1': self.solution_state.results['p1'].path,
                'p2': self.solution_state.results['p2'].path}


if __name__ == '__main__':
    from utils import parse_map_from_file
    layout = parse_map_from_file('small')
    starts = {'p1': (1, 5), 'p2': (2, 6)}
    goal = {'p1': (5, 5), 'p2': (3, 3)}
    controller = Controller(layout, starts, goal)
    controller.find_solution()
    print(controller.get_solution())
