from itertools import accumulate

def running_min(iterable):
    "Smallest of values seen so far."
    # running_min([37, 33, 38, 28]) → 37 33 33 28
    return accumulate(iterable, func=min)
