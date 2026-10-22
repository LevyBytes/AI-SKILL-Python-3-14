# multiprocessing: `multiprocessing.Process`

### `Process` and exceptions

 *class *multiprocessing.Process(*group=None*, *target=None*, *name=None*, *args=()*, *kwargs={}*, ***, *daemon=None*)

A Process object stands for work carried out inside its own separate process. Every method of [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) has a counterpart on the `Process` class.

Always call the constructor with keyword arguments. *group* should always be `None`; its sole reason for existing is parity with [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread). *target* names the callable that the `run()` method will invoke. It defaults to `None`, so nothing gets called. *name* is the process name (consult `name` for further detail). *args* holds the argument tuple for the target call. *kwargs* holds a dictionary of keyword arguments for that same call. When supplied, the keyword-only *daemon* argument flips the process `daemon` flag to either `True` or `False`. Left at `None` (the default), that flag is inherited from the process doing the creating.

Out of the box, *target* receives no arguments. To hand *target* a list or tuple of arguments, set the *args* argument, whose default is `()`.

Any subclass overriding the constructor has to be sure it calls the base class constructor (`super().__init__()`) before it touches anything else on the process.

Note

As a rule, every argument given to `Process` must be picklable. This crops up often when someone tries to build a `Process` or employ a [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) from a REPL using a locally defined *target* function.

Handing in a callable object defined inside the active REPL session makes the child process die at startup with an uncaught [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) exception, since *target* must live inside an importable module to be loaded back during unpickling.

Example of this uncatchable error from the child:

```python
>>> import multiprocessing as mp
>>> def knigit():
...     print("Ni!")
...
>>> process = mp.Process(target=knigit)
>>> process.start()
>>> Traceback (most recent call last):
  File ".../multiprocessing/spawn.py", line ..., in spawn_main
  File ".../multiprocessing/spawn.py", line ..., in _main
AttributeError: module '__main__' has no attribute 'knigit'
>>> process
<SpawnProcess name='SpawnProcess-1' pid=379473 parent=378707 stopped exitcode=1>

```

See The spawn and forkserver start methods. This limitation does not apply when the `"fork"` start method is in use, though as of Python `3.14` that method is no longer the default anywhere. See Contexts and start methods. See also [gh-132898](https://github.com/python/cpython/issues/132898).

Changed in version 3.3: Added the *daemon* parameter.

[Subject index](INDEX.md) · [Previous](global-start-method.md) · [Continue](process-run-start-join-and-liveness.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
