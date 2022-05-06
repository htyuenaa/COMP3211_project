from multiprocessing import Process, Lock
from database_set import Dataset
from main import *


if __name__ == '__main__':
    # run_random_search(agent)
    processes = []
    agents = []
    lock = Lock()
    ds1 = Dataset(agent='p1', map_size=map_name, possible_positions=possible_positions)
    ds2 = Dataset(agent='p2', map_size=map_name, possible_positions=possible_positions)

    def terminate_all():
        for p in processes:
            if p.is_alive():
                p.terminate()
        for p in processes:
            if not p.is_alive():
                p.close()

    def create_process(lock=lock, agent=None, iterations=50):
        lock.acquire()
        if agent is None:
            agent = get_agent()
        db = Dataset(agent=agent, map_size=map_name, possible_positions=possible_positions)
        p = Process(target=run_random_search, args=(agent, db, lock, iterations, len(processes)))
        p.start()
        processes.append(p)
        agents.append(agent)
        lock.release()

    def print_process_status():
        for p in processes:
            print(p)

    def load_and_print_databases(lock=lock, dataset1=ds1, dataset2=ds2):
        lock2 = Lock()
        lock2.acquire()
        dataset1.load_from_file(lock)
        dataset2.load_from_file(lock)
        # db1 = Database(agent='p1', map_size=map_name, possible_positions=possible_positions)
        # db2 = Database(agent='p2', map_size=map_name, possible_positions=possible_positions)
        print(dataset1)
        print(dataset2)
        lock2.release()

    a = ['p2', 'p2', 'p2', 'p2', 'p1', 'p1', 'p1']
    for agent in a:
        create_process(lock, agent)
    load_and_print_databases()
