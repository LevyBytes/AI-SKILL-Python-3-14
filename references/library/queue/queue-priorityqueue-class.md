# queue: `queue.PriorityQueue`

*class *queue.PriorityQueue(*maxsize=0*)

Constructor for a priority queue. *maxsize* is an integer setting the upperbound limit on how many items may sit in the queue. Insertion blocks once that size has been hit, until queue items get consumed. Should *maxsize* be less than or equal to zero, the queue size runs infinite.

The lowest valued entries come back first (the lowest valued entry is whichever one `min(entries)` would return). A common shape for entries is a tuple of the form: `(priority_number, data)`.

Should the *data* elements not be comparable, the data may be tucked inside a class that disregards the data item and weighs only the priority number:

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

```

[Subject index](INDEX.md) · [Previous](queue-lifoqueue-class.md) · [Continue](queue-simplequeue-class.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
