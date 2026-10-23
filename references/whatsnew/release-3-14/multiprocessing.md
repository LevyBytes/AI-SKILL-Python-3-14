# What's new in Python 3.14 / multiprocessing - multiprocessing, pickle, signal

### multiprocessing

- Across Unix systems apart from macOS, [‘forkserver’](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-forkserver) now serves as the default [start method](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods), taking over from [‘fork’](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-fork). Neither Windows nor macOS is touched by this update, since on those platforms [‘spawn’](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-spawn) continues to be the default start method.

Should the threading-unsafe *fork* method be needed, you have to ask for it directly through a context produced by [`get_context()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_context) (the recommended route) or adjust the global default with [`set_start_method()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_start_method).

Consult [forkserver restrictions](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-programming-forkserver) for details, for how it diverges from the *fork* method, and for the ways this update could disrupt current code relying on mutable global shared variables and/or shared objects that fail to be automatically [`pickled`](https://docs.python.org/3.14/library/pickle.html#module-pickle).

(Contributed by Gregory P. Smith in [gh-84559](https://github.com/python/cpython/issues/84559).)

- The `'forkserver'` start method of [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) now authenticates its control socket so that it no longer depends purely on filesystem permissions to limit which other processes could prompt the forkserver into spawning workers and executing code. (Contributed by Gregory P. Smith for [gh-97514](https://github.com/python/cpython/issues/97514).)

- The [multiprocessing proxy objects](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-proxy-objects) covering *list* and *dict* types pick up methods that had been missing before:

>
  - `clear()` and `copy()` for proxies of [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)

  - [`fromkeys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.fromkeys), `reversed(d)`, `d | {}`, `{} | d`, `d |= {'b': 2}` for proxies of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)

(Contributed by Roy Hyunjin Han for [gh-103134](https://github.com/python/cpython/issues/103134).)

- Shared [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) objects are now backed through [`SyncManager.set()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.set), and the [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) method on [`Manager()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Manager) can now be used. (Work by Mingyu Park in [gh-129949](https://github.com/python/cpython/issues/129949).)

- Add the [`interrupt()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.interrupt) to [`multiprocessing.Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) objects, which ends the child process by delivering a [`SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT). With this, [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clauses can emit a stack trace for the process that was halted. (Contributed by Artem Pulkin in [gh-131913](https://github.com/python/cpython/issues/131913).)

[Subject index](INDEX.md) · [Previous source section](mimetypes-add-7z-application-x-7z-compressed-7z.md) · [Next source section](operator.md) · [Release/subject declaration](summary-release-highlights.md)
