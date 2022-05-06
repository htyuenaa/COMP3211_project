from multiprocessing import Process, Lock

from main import *


if __name__ == '__main__':
    # run_random_search(agent)
    processes = []
    agents = []
    lock = Lock()
    db1 = Database(agent='p1', map_size=map_name, possible_positions=possible_positions)
    db2 = Database(agent='p2', map_size=map_name, possible_positions=possible_positions)

    def terminate_all():
        for p in processes:
            if p.is_alive():
                p.terminate()
        for p in processes:
            if not p.is_alive():
                p.close()

    def create_process(lock=lock, agent=None):
        lock.acquire()
        if agent is None:
            agent = get_agent()
        db = Database(agent=agent, map_size=map_name, possible_positions=possible_positions)
        p = Process(target=run_random_search, args=(agent, db, lock, 100, len(processes)))
        p.start()
        processes.append(p)
        agents.append(agent)
        lock.release()

    def print_process_status():
        for p in processes:
            print(p)

    def load_and_print_databases(lock=lock, db1=db1, db2=db2):
        lock.acquire()
        db1.load_from_file(lock)
        db2.load_from_file(lock)
        # db1 = Database(agent='p1', map_size=map_name, possible_positions=possible_positions)
        # db2 = Database(agent='p2', map_size=map_name, possible_positions=possible_positions)
        print(db1)
        print(db2)
        lock.release()

    a = ['p2', 'p2', 'p2', 'p2', 'p1', 'p1', 'p1']
    for agent in a:
        create_process(lock, agent)
