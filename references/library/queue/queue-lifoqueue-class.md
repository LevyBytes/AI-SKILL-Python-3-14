# queue: `queue.LifoQueue`

*class *queue.LifoQueue(*maxsize=0*)

Constructor for a LIFO queue. *maxsize* is an integer setting the upperbound limit on how many items may sit in the queue. Insertion blocks once that size has been hit, until queue items get consumed. Should *maxsize* be less than or equal to zero, the queue size runs infinite.

[Subject index](INDEX.md) · [Previous](queue-queue-class.md) · [Continue](queue-priorityqueue-class.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
