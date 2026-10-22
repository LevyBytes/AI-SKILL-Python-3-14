# heapq — Priority Queue Implementation Notes

### Priority Queue Implementation Notes

One frequent application of a heap is a [priority queue](https://en.wikipedia.org/wiki/Priority_queue), and building one raises a handful of implementation difficulties:

- Sort stability: when two tasks carry equal priorities, how do you ensure they come back out in their original insertion order?

- Comparing (priority, task) pairs as tuples falls apart once the priorities tie and the tasks lack any default ordering of their own.

- When a task's priority shifts, what's the way to relocate it within the heap?

- And when a queued task has to go, how do you track it down and pull it out of the queue?

The first two difficulties can be resolved by holding each entry as a 3-element list made up of the priority, an entry count, and the task. That entry count acts as a tie-breaker, so two tasks sharing a priority come back in the order they went in. And because no two entry counts coincide, the tuple comparison will never wind up comparing two tasks head-to-head.

A further way to handle non-comparable tasks is to build a wrapper class that disregards the task item and compares only the priority field:

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

```

What's left is locating a pending task and then either altering its priority or dropping it entirely. You can locate a task by keeping a dictionary that points at an entry in the queue.

Dropping that entry or revising its priority is trickier, since either would violate the heap structure invariants. One workable approach, then, is to flag the entry as removed and push a fresh entry carrying the updated priority:

```python
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

```

[Subject index](INDEX.md) · [Previous](other-applications.md) · [Continue](theory.md) · [Owning module, declaration or section: heapq](heapq-heapify-to-heapq-heappushpop-max.md)
