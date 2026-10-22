# What's New In Python 3.2 / threading — threading

### threading

A fresh [`Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier) synchronization class has joined the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module; it holds several threads back until each one has arrived at a shared barrier point. Barriers help guarantee that a task carrying multiple preconditions stays idle until every one of its predecessor tasks has finished.

Any number of threads can be handled by a barrier. That generalizes a [Rendezvous](https://en.wikipedia.org/wiki/Synchronous_rendezvous), which applies to just two threads.

Built as a two-phase cyclic barrier, [`Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier) objects fit nicely inside loops. The distinct *filling* and *draining* phases guarantee that every thread is released (drained) before any single thread can circle back and re-enter the barrier. After each cycle the barrier resets completely.

A barrier-usage example:

```python
from threading import Barrier, Thread

def get_votes(site):
    ballots = conduct_election(site)
    all_polls_closed.wait()        # do not count until all polls are closed
    totals = summarize(ballots)
    publish(site, totals)

all_polls_closed = Barrier(len(sites))
for site in sites:
    Thread(target=get_votes, args=(site,)).start()

```

Here the barrier imposes a rule that no polling site may tally votes before every poll has closed. Observe that a barrier-based solution resembles one built on [`threading.Thread.join()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join), except the threads remain alive and keep working (summarizing ballots) once the barrier point has been passed.

Where any of the predecessor tasks might stall or run late, a barrier may be made with an optional *timeout* parameter. Then, should the timeout window pass before all predecessor tasks arrive at the barrier point, every waiting thread is freed and a [`BrokenBarrierError`](https://docs.python.org/3.14/library/threading.html#threading.BrokenBarrierError) exception gets raised:

```python
def get_votes(site):
    ballots = conduct_election(site)
    try:
        all_polls_closed.wait(timeout=midnight - time.now())
    except BrokenBarrierError:
        lockbox = seal_ballots(ballots)
        queue.put(lockbox)
    else:
        totals = summarize(ballots)
        publish(site, totals)

```

Here the barrier enforces a sturdier rule. Should some election sites fail to wrap up ahead of midnight, the barrier times-out and the ballots are sealed then placed into a queue to be dealt with later.

For further demonstrations of how barriers serve parallel computing, see [Barrier Synchronization Patterns](https://osl.cs.illinois.edu/media/papers/karmani-2009-barrier_synchronization_pattern.pdf). There is also a plain yet complete account of barriers in [The Little Book of Semaphores](https://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf), *section 3.6*.

(Built by Kristján Valur Jónsson, whose API got reviewed by Jeffrey Yasskin, in [bpo-8777](https://bugs.python.org/issue?@action=redirect&bpo=8777).)

[Subject index](INDEX.md) · [Previous source section](collections.md) · [Next source section](datetime-and-time.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
