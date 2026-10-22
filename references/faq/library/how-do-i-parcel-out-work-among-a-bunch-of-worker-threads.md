# How do I parcel out work among a bunch of worker threads?

### How do I parcel out work among a bunch of worker threads?

The simplest route is the [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) module, and in particular the [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) class.

Alternatively, when you want tight control over how dispatching works, you can hand-roll the logic yourself. Reach for the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module to build a queue holding a list of jobs. The [`Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) class keeps a list of objects, offering a `.put(obj)` method that enqueues items along with a `.get()` method that hands them back. Whatever locking is needed to guarantee each job is dispensed exactly once is handled by the class itself.

A trivial example follows:

```python
import threading, queue, time

# The worker thread gets jobs off the queue.  When the queue is empty, it
# assumes there will be no more work and exits.
# (Realistically workers will run until terminated.)
def worker():
    print('Running worker')
    time.sleep(0.1)
    while True:
        try:
            arg = q.get(block=False)
        except queue.Empty:
            print('Worker', threading.current_thread(), end=' ')
            print('queue empty')
            break
        else:
            print('Worker', threading.current_thread(), end=' ')
            print('running with argument', arg)
            time.sleep(0.5)

# Create queue
q = queue.Queue()

# Start a pool of 5 workers
for i in range(5):
    t = threading.Thread(target=worker, name='worker %i' % (i+1))
    t.start()

# Begin adding work to the queue
for i in range(50):
    q.put(i)

# Give threads time to run
print('Main thread sleeping')
time.sleep(5)

```

Running it yields the output below:

```none
Running worker
Running worker
Running worker
Running worker
Running worker
Main thread sleeping
Worker <Thread(worker 1, started 130283832797456)> running with argument 0
Worker <Thread(worker 2, started 130283824404752)> running with argument 1
Worker <Thread(worker 3, started 130283816012048)> running with argument 2
Worker <Thread(worker 4, started 130283807619344)> running with argument 3
Worker <Thread(worker 5, started 130283799226640)> running with argument 4
Worker <Thread(worker 1, started 130283832797456)> running with argument 5
...

```

See the module's documentation for additional detail; a feature-rich interface is provided by the [`Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) class.

[Subject index](INDEX.md)
