# queue — Waiting for task completion

### Waiting for task completion

Example of how to wait on enqueued tasks reaching completion:

```python
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')

```

[Subject index](INDEX.md) · [Previous](queue-qsize-to-queue-join.md) · [Continue](queue-shutdown.md) · [Owning module, declaration or section: queue](queue-queue-class.md)
