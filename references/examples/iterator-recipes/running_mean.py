from itertools import accumulate, count
from operator import truediv

def running_mean(iterable):
    "Average of values seen so far."
    # running_mean([37, 33, 38, 28]) → 37 35 36 34
    return map(truediv, accumulate(iterable), count(1))
