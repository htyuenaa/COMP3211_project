import time

from search import a_star_search
from datetime import datetime
from database import Database
from result import Result
from utils import *


def run_and_print_result(starting, agent, database=None, lock=None):
    if lock is not None:  # prevent other processes to print at the same time
        lock.acquire()
    print(agent)
    init_time = datetime.now()
    print(f'current time: {init_time}')
    print(f'finding path for initial position: {starting}...')
    if lock is not None:  # release lock for other processes to print
        lock.release()

    path = a_star_search(layout, start=starting, end=goals[map_name][agent], database=database)

    if lock is not None:  # prevent other processes to print at the same time
        lock.acquire()
    print(f'finding path for {agent} initial position: {starting} done!')
    print(f'time taken: {datetime.now() - init_time}')
    print(f'path: {path}')
    print(f'cost: {len(path)}')
    if lock is not None:  # release lock for other processes to print
        lock.release()
    return path


def performance_test(agent):
    db = Database(agent=agent, map_size=map_name, possible_positions=possible_positions)
    init_pos = (6, 122)
    # print('run without database')
    # path = run_and_print_result(init_pos)
    print('run with database')
    path = run_and_print_result(init_pos, agent, db)
    result = Result(init_pos=init_pos, path=path)
    db.add_this_and_other_results(result)
    # db.save_to_file()


def run_random_search(agent, db, lock=None, num_of_searches=100, thread_number=0):
    for i in range(num_of_searches):
        db.load_from_file(lock)
        print(f'Thread number {thread_number}: {i} iteration')
        init_pos = db.get_random_init_pos()
        if init_pos is None:
            print('The searching is done!')
            exit()
        path = run_and_print_result(init_pos, agent, db, lock)
        result = Result(init_pos=init_pos, path=path)

        if lock is not None:  # prevent other processes to save it at the same time
            lock.acquire()
        db.add_this_and_other_results(result)
        db.save_to_file()
        time.sleep(1.5)
        if lock is not None:
            lock.release()


if __name__ == '__main__':
    agent = get_agent()
    performance_test(agent)
    # run_random_search(agent)
