# What's new in Python 3.14 / concurrent.futures - concurrent.futures, concurrent.interpreters, multiprocessing, pickle

### concurrent.futures

- A new executor class arrives, [`InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor), which surfaces several Python interpreters inside one process ("subinterpreters") for Python code to use. It relies on a pool of separate Python interpreters that run calls asynchronously.

It stands apart from the fresh [`interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters) module that PEP 734 brought in. (Contributed by Eric Snow in [gh-124548](https://github.com/python/cpython/issues/124548).)

- Across Unix platforms apart from macOS, ["forkserver"](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-forkserver) has become the default [start method](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods) used by [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) (taking over from ["fork"](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-fork)). Neither Windows nor macOS are touched by this change, since on both ["spawn"](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-spawn) stays the default start method.

Should you need the threading incompatible *fork* method, request it directly by handing a multiprocessing context *mp_context* over to [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor).

Consult [forkserver restrictions](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-programming-forkserver) to learn the details and the contrasts versus the *fork* method, plus the ways this change can touch existing code holding mutable global shared variables and/or shared objects that cannot get automatically [`pickled`](https://docs.python.org/3.14/library/pickle.html#module-pickle).

(Contributed by Gregory P. Smith in [gh-84559](https://github.com/python/cpython/issues/84559).)

- Two fresh methods join [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), namely [`terminate_workers()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.terminate_workers) and [`kill_workers()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.kill_workers), giving you the means to terminate or kill every live worker process within a given pool. (Contributed by Charles Machalow in [gh-130849](https://github.com/python/cpython/issues/130849).)

- The optional *buffersize* parameter joins [`Executor.map`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map) so you can cap how many submitted tasks still have unyielded results. Once that buffer fills, iterating across the *iterables* halts until some result leaves the buffer. (Contributed by Enzo Bonnal and Josh Rosenberg in [gh-74028](https://github.com/python/cpython/issues/74028).)

[Subject index](INDEX.md) · [Previous source section](calendar.md) · [Next source section](configparser.md) · [Release/subject declaration](summary-release-highlights.md)
