# multiprocessing: `multiprocessing.set_executable()`, `multiprocessing.set_forkserver_preload()`, `multiprocessing.set_start_method()`

multiprocessing.set_executable(*executable*)

Point at the Python interpreter to launch when starting a child process. (By default [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) is the one used.) Embedders will likely have to run something along the lines of

```python
set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))

```

before child processes can be created.

Changed in version 3.4: Gained POSIX support whenever the `'spawn'` start method is in use.

Changed in version 3.11: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 multiprocessing.set_forkserver_preload(*module_names*)

Hand the forkserver main process a list of module names to try importing, so that their already-imported state passes down to forked processes. An [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) during this is quietly ignored. This serves as a performance boost by sparing repeated work in each process.

For it to take effect, you must call it before the forkserver process gets launched (before making a `Pool` or starting a `Process`).

It carries meaning only with the `'forkserver'` start method in use. See Contexts and start methods.

Added in version 3.4.

 multiprocessing.set_start_method(*method*, *force=False*)

Pick which method launches child processes. For the *method* argument, `'fork'`, `'spawn'` or `'forkserver'` are accepted. Raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) when the start method is already set while *force* is not `True`. When *method* is `None` and *force* is `True`, the start method gets set to `None`. When *method* is `None` and *force* is `False`, the context gets set to the default context.

Be aware this should be called no more than once, and it should sit inside the `if __name__ == '__main__'` clause of the main module.

See Contexts and start methods.

Added in version 3.4.

Note

`multiprocessing` offers no counterparts to [`threading.active_count()`](https://docs.python.org/3.14/library/threading.html#threading.active_count), [`threading.enumerate()`](https://docs.python.org/3.14/library/threading.html#threading.enumerate), [`threading.settrace()`](https://docs.python.org/3.14/library/threading.html#threading.settrace), [`threading.setprofile()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile), [`threading.Timer`](https://docs.python.org/3.14/library/threading.html#threading.Timer), or [`threading.local`](https://docs.python.org/3.14/library/threading.html#threading.local).

[Subject index](INDEX.md) · [Previous](active-children-and-start-method-discovery.md) · [Continue](multiprocessing-connection-connection-class-to-send.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Miscellaneous](active-children-and-start-method-discovery.md)
