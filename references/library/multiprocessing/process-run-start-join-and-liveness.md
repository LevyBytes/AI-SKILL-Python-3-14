# multiprocessing.Process: `run()`, `start()`, `join()`, `is_alive()`

run()

Method representing the process's activity.

A subclass may override this method. The default `run()` method calls the callable object that was handed to the object's constructor as the target argument, if there is one, passing positional and keyword arguments drawn from the *args* and *kwargs* arguments respectively.

Supplying a list or tuple for the *args* argument given to `Process` produces the same result.

Example:

```python
>>> from multiprocessing import Process
>>> p = Process(target=print, args=[1])
>>> p.run()
1
>>> p = Process(target=print, args=(1,))
>>> p.run()
1

```

 start()

Start the process's activity.

You may call this at most once per process object. It sets things up so the object's `run()` method runs in a separate process.

 join([*timeout*])

When the optional *timeout* argument is `None` (the default), the method blocks until the process whose `join()` method was called finishes. If *timeout* is a positive number, it blocks for at most *timeout* seconds. Note that the method returns `None` whether its process finishes or the call times out. Inspect the process's `exitcode` to find out whether it ended.

A process can be joined many times.

A process cannot join itself, since doing so would deadlock. Trying to join a process that has not yet been started is an error.

 name

The process's name. The name is a string used purely for identification. It carries no semantics. Several processes can be given the same name.

The constructor sets the initial name. When no name is explicitly given to the constructor, one of the form 'Process-N1:N2:...:Nk' is built, where each Nk is the N-th child of its parent.

 is_alive()

Return whether the process is alive.

Loosely speaking, a process object is alive from the instant the `start()` method returns up to the moment the child process ends.

 daemon

The process's daemon flag, a Boolean value. You must set it before `start()` is called.

The initial value is inherited from the creating process.

As a process exits, it tries to terminate every one of its daemonic child processes.

Note that a daemonic process is barred from creating child processes. Otherwise a daemonic process would orphan its children should it be terminated when its parent process exits. Furthermore, these are **not** Unix daemons or services; they are ordinary processes that get terminated (and not joined) once the non-daemonic processes have exited.

On top of the [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) API, `Process` objects additionally support the following attributes and methods:

 pid

Return the process ID. Before the process is spawned, this will be `None`.

 exitcode

The child's exit code. As long as the process has not yet finished, this stays `None`.

A normal return from the child's `run()` method yields an exit code of 0. Should it finish through [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) given an integer argument *N*, the exit code becomes *N*.

If the child ended because of an exception that `run()` did not catch, the exit code will be 1. If a signal *N* terminated it, the exit code will be the negative value *-N*.

 authkey

The process's authentication key (a byte string).

[Subject index](INDEX.md) · [Previous](multiprocessing-process-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.Process](multiprocessing-process-class.md) · [Owning module, declaration or section: `Process` and exceptions](multiprocessing-process-class.md) · [Required continuation of the source contract](process-interrupt-terminate-kill-and-close.md)
