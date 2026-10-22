from contextlib import suppress
from heapq import heappush, heappushpop, heappush_max, heappushpop_max

def running_median(iterable):
    "Median of values seen so far."
    # running_median([37, 33, 38, 28]) → 37 35 37 35
    read = iter(iterable).__next__
    lo = []  # max-heap
    hi = []  # min-heap the same size as or one smaller than lo
    with suppress(StopIteration):
        while True:
            heappush_max(lo, heappushpop(hi, read()))
            yield lo[0]
            heappush(hi, heappushpop_max(lo, read()))
            yield (lo[0] + hi[0]) / 2
