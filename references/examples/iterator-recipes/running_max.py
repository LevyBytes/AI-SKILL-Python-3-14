from itertools import accumulate

def running_max(iterable):
    "Largest of values seen so far."
    # running_max([37, 33, 38, 28]) → 37 37 38 38
    return accumulate(iterable, func=max)
