from search import a_star_search
from datetime import datetime
from database import Database
from result import Result
from utils import *


def run_and_print_result(starting, database=None):
    print(f'finding path for initial position: {starting}...')
    init_time = datetime.now()
    path = a_star_search(layout, start=starting, end=goal, database=database)
    print(f'time taken: {datetime.now() - init_time}')
    print(f'path: {path}')
    print(f'cost: {len(path)}')
    return path


if __name__ == '__main__':
    db = Database(agent=agent, map_size=map_name, possible_positions=possible_positions)
    for i in range(100):
        print(f'iteration {i}')
        init_pos = db.get_random_init_pos()
        # init_pos = (205, 255)
        # path = run_and_print_result(init_pos)
        path = run_and_print_result(init_pos, db)
        result = Result(init_pos=init_pos, path=path)
        db.add_this_and_other_results(result)
        db.save_to_file()

