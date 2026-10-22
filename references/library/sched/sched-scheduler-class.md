# sched — `sched` — Event scheduler

## sched — Event scheduler

### `sched` — Event scheduler

**Source code:** [Lib/sched.py](https://github.com/python/cpython/tree/3.14/Lib/sched.py)

---

A class implementing a general purpose event scheduler is defined by the `sched` module:

 *class *sched.scheduler(*timefunc=time.monotonic*, *delayfunc=time.sleep*)

A generic interface for scheduling events is defined by the `scheduler` class. To actually engage with the "outside world" it relies on two functions — *timefunc* must be callable with no arguments and give back a number (the "time", measured in any units you like). The *delayfunc* function must be callable with one argument matching the output of *timefunc*, and is expected to pause for that many time units. *delayfunc* also gets invoked with the argument `0` after each event runs, which gives other threads a chance to run in multi-threaded applications.

Changed in version 3.3: *timefunc* and *delayfunc* parameters are optional.

Changed in version 3.3: It became safe to use the `scheduler` class across multiple threads.

Example:

```python
>>> import sched, time
>>> s = sched.scheduler(time.time, time.sleep)
>>> def print_time(a='default'):
...     print("From print_time", time.time(), a)
...
>>> def print_some_times():
...     print(time.time())
...     s.enter(10, 1, print_time)
...     s.enter(5, 2, print_time, argument=('positional',))
...     # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
...     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
...     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
...     s.run()
...     print(time.time())
...
>>> print_some_times()
1652342830.3640375
From print_time 1652342830.3642538 second enterabs
From print_time 1652342830.3643398 first enterabs
From print_time 1652342835.3694863 positional
From print_time 1652342835.3696074 keyword
From print_time 1652342840.369612 default
1652342840.3697174

```

[Subject index](INDEX.md) · [Continue](scheduler-enterabs-to-scheduler-queue.md)
