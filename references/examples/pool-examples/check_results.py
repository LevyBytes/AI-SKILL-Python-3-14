import multiprocessing
import time
import random
import sys
from pool_workers import *

def check_results(pool):
    TASKS = [(mul, (i, 7)) for i in range(10)] + \
            [(plus, (i, 8)) for i in range(10)]
    results = [pool.apply_async(calculate, t) for t in TASKS]
    imap_it = pool.imap(calculatestar, TASKS)
    imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)
    print('Ordered results using pool.apply_async():')
    for r in results:
        print('\t', r.get())
    print()
    print('Ordered results using pool.imap():')
    for x in imap_it:
        print('\t', x)
    print()
    print('Unordered results using pool.imap_unordered():')
    for x in imap_unordered_it:
        print('\t', x)
    print()
    print('Ordered results using pool.map() --- will block till complete:')
    for x in pool.map(calculatestar, TASKS):
        print('\t', x)
    print()
    print('Testing error handling:')
    return TASKS
