from itertools import count, tee
from running_max import running_max
from running_mean import running_mean
from running_median import running_median
from running_min import running_min

def running_statistics(iterable):
    "Aggregate statistics for values seen so far."
    # Generate tuples:  (size, minimum, median, maximum, mean)
    t0, t1, t2, t3 = tee(iterable, 4)
    return zip(
        count(1),
        running_min(t0),
        running_median(t1),
        running_max(t2),
        running_mean(t3),
    )
