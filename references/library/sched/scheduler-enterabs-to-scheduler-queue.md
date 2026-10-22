# sched — Scheduler Objects

### Scheduler Objects

These methods and attributes belong to `scheduler` instances:

 scheduler.enterabs(*time*, *priority*, *action*, *argument=()*, *kwargs={}*)

Queue up a new event. The *time* argument is expected to be a numeric type matching the return value of the *timefunc* function handed to the constructor. Events queued for the same *time* run in the order of their *priority*. A lower number stands for a higher priority.

Running the event amounts to running `action(*argument, **kwargs)`. *argument* is a sequence carrying the positional arguments for *action*. *kwargs* is a dictionary carrying the keyword arguments for *action*.

The return value is an event that you can use to cancel the event later on (see `cancel()`).

Changed in version 3.3: *argument* parameter is optional.

Changed in version 3.3: *kwargs* parameter was added.

 scheduler.enter(*delay*, *priority*, *action*, *argument=()*, *kwargs={}*)

Queue up an event for *delay* additional time units. Aside from the relative time, the remaining arguments, the effect, and the return value match those of `enterabs()`.

Changed in version 3.3: *argument* parameter is optional.

Changed in version 3.3: *kwargs* parameter was added.

 scheduler.cancel(*event*)

Take the event out of the queue. When *event* is not an event presently in the queue, this method will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 scheduler.empty()

Return `True` if the event queue is empty.

 scheduler.run(*blocking=True*)

Run every scheduled event. Using the *delayfunc* function handed to the constructor, this method waits for the next event, then runs it, and continues like that until no scheduled events are left.

When *blocking* is false, it immediately runs whatever events in the queue carry a time value at or below the current *timefunc* value (if any) and returns the difference between the present *timefunc* reading and the time value attached to the queue's next pending event. When the queue is empty, it gives back `None`.

An exception may be raised by either *action* or *delayfunc*. Either way, the scheduler keeps a consistent state and lets the exception propagate. When *action* raises an exception, that event will not be retried in later calls to `run()`.

When a series of events takes longer to run than the time left before the next event, the scheduler simply falls behind. No events get dropped; it falls to the calling code to cancel events that are no longer relevant.

Changed in version 3.3: *blocking* parameter was added.

 scheduler.queue

A read-only attribute giving back a list of the events still to come, in the order they will run. Each event appears as a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying the following fields: time, priority, action, argument, kwargs.

[Subject index](INDEX.md) · [Previous](sched-scheduler-class.md) · [Continue](../secrets/secrets-generate-secure-random-numbers-for-managing-secrets.md) · [Owning module, declaration or section: sched](sched-scheduler-class.md)
