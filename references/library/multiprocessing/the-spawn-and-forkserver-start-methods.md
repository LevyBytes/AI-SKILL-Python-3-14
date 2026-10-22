# multiprocessing — The *spawn* and *forkserver* start methods

### The *spawn* and *forkserver* start methods

A handful of extra restrictions apply here that the *fork* start method does not carry.

More picklability

>

Make sure that every argument to `Process` is picklable. Also, when you subclass `Process.__init__`, you have to make certain instances will be picklable by the time the `Process.start` method gets called.

Global variables

>

Keep in mind that when code running in a child process tries to reach a global variable, the value it sees (if any) may differ from the value held in the parent process at the moment `Process.start` was called.

Global variables that are merely module-level constants, however, raise no trouble.

Safe importing of main module

>

Make certain the main module can be imported safely by a new Python interpreter without setting off unintended side effects (such as launching a new process).

For instance, with the *spawn* or *forkserver* start method, running the module below would fail with a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError):

```python
from multiprocessing import Process

def foo():
    print('hello')

p = Process(target=foo)
p.start()

```

Instead you should guard the program's “entry point” with `if __name__ == '__main__':`, like so:

```python
from multiprocessing import Process, freeze_support, set_start_method

def foo():
    print('hello')

if __name__ == '__main__':
    freeze_support()
    set_start_method('spawn')
    p = Process(target=foo)
    p.start()

```

(You may drop the `freeze_support()` line when the program is to run normally rather than frozen.)

This lets the freshly spawned Python interpreter import the module safely and then run the module's `foo()` function.

Comparable restrictions kick in whenever a pool or manager gets created within the main module.

[Subject index](INDEX.md) · [Previous](process-start-lock-example.md) · [Continue](examples.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
