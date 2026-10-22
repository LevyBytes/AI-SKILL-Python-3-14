# runpy: `runpy.run_path()`

runpy.run_path(*path_name*, *init_globals=None*, *run_name=None*)

Run the code found at the given filesystem location and hand back the resulting module's globals dictionary. Just as with a script name handed to the CPython command line, *file_path* may point at a Python source file, a compiled bytecode file, or a valid [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entry holding a [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module (for example, a zipfile that contains a top-level `__main__.py` file).

For a plain script, the given code simply runs inside a fresh module namespace. For a valid [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entry (usually a zipfile or directory), the entry is first prepended to `sys.path`. Then the function hunts for a [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module along the updated path and runs it. Note that nothing specifically guards against running an existing `__main__` entry found somewhere else on `sys.path` if no such module exists at the specified location.

The optional dictionary argument *init_globals* lets you seed the module's globals dictionary ahead of running the code. *init_globals* stays unmodified. Should any of the special global variables listed below already exist in *init_globals*, `run_path()` overrides those definitions.

Before the module code runs, the special global variables `__name__`, `__spec__`, `__file__`, `__cached__`, `__loader__` and `__package__` get set in the globals dictionary. (Bear in mind that this is the minimal set of variables — additional ones may get set implicitly as an interpreter implementation detail.)

`__name__` becomes *run_name* when this optional argument is not [`None`](https://docs.python.org/3.14/library/constants.html#None) and otherwise becomes `'<run_path>'`.

When *file_path* points straight at a script file (be it source or precompiled byte code), then `__file__` gets set to *file_path*, while `__spec__`, `__cached__`, `__loader__` and `__package__` are each set to [`None`](https://docs.python.org/3.14/library/constants.html#None).

When *file_path* points at a valid [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entry, then `__spec__` gets set to suit the imported [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module (meaning `__spec__.name` will always be `__main__`). `__file__`, `__cached__`, `__loader__` and `__package__` are [set as normal](https://docs.python.org/3.14/reference/datamodel.html#import-mod-attrs) according to the module spec.

Several modifications also happen to the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module. To begin with, [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) may change as outlined above. `sys.argv[0]` gets refreshed with the value of *file_path* and `sys.modules[__name__]` gets refreshed with a temporary module object standing in for the module being run. Every change made to items in `sys` is undone before the function returns.

Note that, in contrast to `run_module()`, the changes made to [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) are not optional within this function, because these adjustments are what make running [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entries possible. Since the thread-safety constraints still hold, you should either serialise use of this function in threaded code with the import lock or delegate it to a separate process.

See also

[Interface options](https://docs.python.org/3.14/using/cmdline.html#using-on-interface-options) for equivalent functionality on the command line (`python path/to/script`).

Added in version 3.2.

Changed in version 3.4: Reworked to exploit the module spec feature that [**PEP 451**](https://peps.python.org/pep-0451/) brought in. As a result `__cached__` can be set properly whenever `__main__` comes in from a valid [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entry instead of running directly.

Changed in version 3.12: Setting `__cached__`, `__loader__`, and `__package__` is now deprecated.

See also

[**PEP 338**](https://peps.python.org/pep-0338/) – Executing modules as scripts

PEP written and implemented by Nick Coghlan.

[**PEP 366**](https://peps.python.org/pep-0366/) – Main module explicit relative imports

PEP written and implemented by Nick Coghlan.

[**PEP 451**](https://peps.python.org/pep-0451/) – A ModuleSpec Type for the Import System

PEP written and implemented by Eric Snow

[Command line and environment](https://docs.python.org/3.14/using/cmdline.html#using-on-general) - CPython command line details

The [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) function

[Subject index](INDEX.md) · [Previous](runpy-run-module.md) · [Continue](../sched/sched-scheduler-class.md) · [Owning module, declaration or section: runpy](runpy-run-module.md)
