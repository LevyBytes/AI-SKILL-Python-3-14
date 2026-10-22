# multiprocessing: Active children and process start-method discovery

### Miscellaneous

 multiprocessing.active_children()

Give back a list of every live child of the current process.

A side effect of calling this is the “joining” of any processes that have already finished.

 multiprocessing.cpu_count()

Give back how many CPUs the system has.

That count is not the same as how many CPUs the current process is allowed to use. To learn the number of usable CPUs, turn to [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) (or `len(os.sched_getaffinity(0))`).

When the CPU count cannot be worked out, a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised.

See also

[`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count) [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count)

Changed in version 3.13: Since this merely wraps the [`os`](https://docs.python.org/3.14/library/os.html#module-os) cpu count APIs, you may also override what it returns through the [`-X cpu_count`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) flag or [`PYTHON_CPU_COUNT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CPU_COUNT).

 multiprocessing.current_process()

Give back the `Process` object that stands for the current process.

It is the counterpart of [`threading.current_thread()`](https://docs.python.org/3.14/library/threading.html#threading.current_thread).

 multiprocessing.parent_process()

Give back the `Process` object that stands for the parent of the `current_process()`. In the main process, `parent_process` will be `None`.

Added in version 3.8.

 multiprocessing.freeze_support()

Provide support for situations where a `multiprocessing`-using program has been frozen into an executable. (Verified to work with **py2exe**, **PyInstaller** and **cx_Freeze**.)

This function has to be called immediately following the `if __name__ == '__main__'` line of the main module. To illustrate:

```python
from multiprocessing import Process, freeze_support

def f():
    print('hello world!')

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()

```

Leaving out the `freeze_support()` line means an attempt to run the frozen executable will raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

When the start method is not *spawn*, calling `freeze_support()` does nothing. On top of that, if the Python interpreter runs the module in the usual way (the program is unfrozen), `freeze_support()` has no effect.

 multiprocessing.get_all_start_methods()

Gives back a list of the supported start methods, with the default appearing first. The candidate start methods are `'fork'`, `'spawn'` and `'forkserver'`. Support for every method is not present on every platform. See Contexts and start methods.

Added in version 3.4.

 multiprocessing.get_context(*method=None*)

Give back a context object whose attributes match those of the `multiprocessing` module.

When *method* is `None`, the default context comes back. Be aware that should the global start method still be unset, this assigns it the system default. See Global start method for more details. In other cases *method* should be `'fork'`, `'spawn'`, `'forkserver'`. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the named start method is unavailable. See Contexts and start methods.

Added in version 3.4.

 multiprocessing.get_start_method(*allow_none=False*)

Give back the name of the start method used for launching processes.

When the global start method is unset and *allow_none* is `False`, the global start method takes on the default, whose name then comes back. See Global start method for more details.

The value returned can be `'fork'`, `'spawn'`, `'forkserver'` or `None`. See Contexts and start methods.

Added in version 3.4.

Changed in version 3.8: On macOS, *spawn* is now the default start method. Treat the *fork* start method as unsafe, since it may crash the subprocess. See [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).

[Subject index](INDEX.md) · [Previous](joinable-process-queue.md) · [Continue](process-executable-and-start-method-configuration.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
