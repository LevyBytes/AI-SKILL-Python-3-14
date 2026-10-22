# None of my threads seem to run: why?

### None of my threads seem to run: why?

The moment the main thread finishes, every thread is killed. Your main thread runs too fast, leaving the threads no opportunity to accomplish anything.

One easy remedy is to append a sleep at the program's end, long enough that all the threads complete:

```python
import threading, time

def thread_task(name, n):
    for i in range(n):
        print(name, i)

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10)  # <---------------------------!

```

Yet now (on many platforms) the threads fail to run in parallel and instead seem to execute one after another, sequentially! That happens because the OS thread scheduler holds off launching a new thread until the prior thread becomes blocked.

One easy remedy is to insert a tiny sleep at the beginning of the run function:

```python
def thread_task(name, n):
    time.sleep(0.001)  # <--------------------!
    for i in range(n):
        print(name, i)

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10)

```

Rather than guessing at a suitable delay for [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep), a semaphore-style mechanism is the better choice. One approach is to employ the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module to build a queue object, have every thread push a token onto the queue once it finishes, and have the main thread pull as many tokens off the queue as there are threads.

[Subject index](INDEX.md)
