import multiprocessing
from check_results import check_results
from check_errors import check_errors
from check_timeouts import check_timeouts

def test():
    PROCESSES = 4
    print('Creating pool with %d processes\n' % PROCESSES)
    with multiprocessing.Pool(PROCESSES) as pool:
        tasks = check_results(pool)
        check_errors(pool)
        check_timeouts(pool, tasks)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    test()
