# Using concurrent.futures.ProcessPoolExecutor

### Using concurrent.futures.ProcessPoolExecutor

To employ [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) for launching your worker processes, the queue has to be built in a slightly altered manner. Rather than

```python
queue = multiprocessing.Queue(-1)

```

you ought to write

```python
queue = multiprocessing.Manager().Queue(-1)  # also works with the examples above

```

after which the worker-creation block can change from this:

```python
workers = []
for i in range(10):
    worker = multiprocessing.Process(target=worker_process,
                                     args=(queue, worker_configurer))
    workers.append(worker)
    worker.start()
for w in workers:
    w.join()

```

into this (recalling that you must first import [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures)):

```python
with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    for i in range(10):
        executor.submit(worker_process, queue, worker_configurer)

```

[Subject index](INDEX.md) · [Previous source context](imports-listener-configuration-and-whole-queue-listener-loop.md) · [Following source context](deploying-web-applications-using-gunicorn-and-uwsgi.md)
