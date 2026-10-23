# What's New In Python 3.2 / PEP 3148: The `concurrent.futures` module - concurrent.futures

### PEP 3148: The `concurrent.futures` module

The tools for spinning up and coordinating concurrency now live under a new top-level namespace, *concurrent*. Its inaugural component is a *futures* package delivering a single high-level API for overseeing threads and processes.

[`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) drew its design from the *java.util.concurrent* package. Under that scheme, an in-flight call together with whatever it returns is captured by a [`Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) object that abstracts away traits shared by threads, processes, and remote procedure calls. Such an object permits querying state (running or done), specifying timeouts, cancelling, registering callbacks, and retrieving either results or exceptions.

What the module chiefly provides is two executor classes for launching and overseeing calls. Those executors exist to simplify reusing existing tools for issuing parallel calls. They spare you from assembling a resource pool, kicking off the calls, building a results queue, wiring up time-out handling, and capping the overall count of threads, processes, or remote procedure calls.

The ideal arrangement has each application reuse one executor among its various components, keeping process and thread caps under a single point of control. That resolves the design problem that surfaces whenever every component pursues its own rival approach to managing resources.

The two classes expose a shared interface of three methods: [`submit()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.submit) schedules a callable and hands back a [`Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) object; [`map()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map) queues numerous asynchronous calls together; and [`shutdown()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.shutdown) releases resources. Being a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager), the class fits inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, guaranteeing resources get freed once any still-pending futures finish running.

A short [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) demonstration spins up four threads in parallel to copy files:

```python
import concurrent.futures, shutil
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest4.txt')

```

See also

[**PEP 3148**](https://peps.python.org/pep-3148/) - Futures — Execute Computations Asynchronously

PEP written by Brian Quinlan.

[Code for Threaded Parallel URL reads](https://docs.python.org/3.14/library/concurrent.futures.html#threadpoolexecutor-example), an example using threads to fetch multiple web pages in parallel.

[Code for computing prime numbers in parallel](https://docs.python.org/3.14/library/concurrent.futures.html#processpoolexecutor-example), an example demonstrating [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor).

[Subject index](INDEX.md) · [Previous source section](pep-391-dictionary-based-configuration-for-logging.md) · [Next source section](pep-3147-pyc-repository-directories.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
