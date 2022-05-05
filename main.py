from search import a_star_search
from datetime import datetime
from database import Database
from result import Result
from utils import *


def run_and_print_result(starting, database=None):
    print(f'agent: {agent}')
    init_time = datetime.now()
    print(f'current time: {init_time}')
    print(f'finding path for initial position: {starting}...')
    path = a_star_search(layout, start=starting, end=goals[map_name][agent], database=database)
    print(f'time taken: {datetime.now() - init_time}')
    print(f'path: {path}')
    print(f'cost: {len(path)}')
    return path


if __name__ == '__main__':
    agent = get_agent()
    db = Database(agent=agent, map_size=map_name, possible_positions=possible_positions)
    for i in range(1000):
        print(f'iteration {i}')
        init_pos = db.get_random_init_pos()
        if i <= 8:
            init_pos = corners[i]
        if init_pos is None:
            print('The searching is done!')
            exit()
        db.dump()
        path = run_and_print_result(init_pos, db)
        result = Result(init_pos=init_pos, path=path)
        db.load_and_save()
        db.add_this_and_other_results(result)
        db.save_to_file()

