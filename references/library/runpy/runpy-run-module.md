# runpy: `runpy.run_module()`

### `runpy` — Locating and executing Python modules

**Source code:** [Lib/runpy.py](https://github.com/python/cpython/tree/3.14/Lib/runpy.py)

---

Locating and running Python modules without first importing them is the job of the `runpy` module. Its primary purpose is to back the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) command line switch, which lets scripts be found through the Python module namespace rather than through the filesystem.

Keep in mind that this is *not* a sandbox module — all code runs inside the current process, and whatever side effects result (such as cached imports of other modules) stay in place once the functions return.

On top of that, there is no guarantee that any functions and classes the executed code defines will keep working correctly once a `runpy` function returns. Where that constraint will not do for your situation, [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) is probably a better fit than this module.

Two functions are offered by the `runpy` module:

 runpy.run_module(*mod_name*, *init_globals=None*, *run_name=None*, *alter_sys=False*)

Run the code belonging to the named module and hand back the resulting module's globals dictionary. The standard import machinery first locates the module's code (see [**PEP 302**](https://peps.python.org/pep-0302/) for the particulars), which then runs inside a fresh module namespace.

You should pass an absolute module name as the *mod_name* argument. When the module name points at a package rather than an ordinary module, that package is imported, after which the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) submodule contained in that package runs and the resulting module globals dictionary is handed back.

The optional dictionary argument *init_globals* lets you seed the module's globals dictionary ahead of running the code. *init_globals* stays unmodified. Should any of the special global variables listed below already exist in *init_globals*, `run_module()` overrides those definitions.

Before the module code runs, the special global variables `__name__`, `__spec__`, `__file__`, `__cached__`, `__loader__` and `__package__` get set in the globals dictionary. (Bear in mind that this is the minimal set of variables — additional ones may get set implicitly as an interpreter implementation detail.)

`__name__` becomes *run_name* when this optional argument is not [`None`](https://docs.python.org/3.14/library/constants.html#None), becomes `mod_name + '.__main__'` when the named module is a package, and otherwise becomes the *mod_name* argument.

`__spec__` gets set to suit the module that was *actually* imported (meaning `__spec__.name` will be either *mod_name* or `mod_name + '.__main__'`, but never *run_name*).

`__file__`, `__cached__`, `__loader__` and `__package__` are [set as normal](https://docs.python.org/3.14/reference/datamodel.html#import-mod-attrs) according to the module spec.

When the *alter_sys* argument is provided and works out to [`True`](https://docs.python.org/3.14/library/constants.html#True), then `sys.argv[0]` gets refreshed with the value of `__file__` and `sys.modules[__name__]` gets refreshed with a temporary module object standing in for the module being run. Both `sys.argv[0]` and `sys.modules[__name__]` revert to their original values before the function returns.

Be aware that this tinkering with [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) is not thread-safe. Other threads might catch the partially initialised module along with the altered argument list. The recommendation is to leave the `sys` module untouched when you call this function from threaded code.

See also

The [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) option providing the same functionality from the command line.

Changed in version 3.1: Gained the capacity to run packages by hunting for a [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) submodule.

Changed in version 3.2: Introduced the `__cached__` global variable (see [**PEP 3147**](https://peps.python.org/pep-3147/)).

Changed in version 3.4: Reworked to exploit the module spec feature that [**PEP 451**](https://peps.python.org/pep-0451/) brought in. As a result `__cached__` can be set properly for modules run by this route, and the genuine module name is always reachable via `__spec__.name`.

Changed in version 3.12: Setting `__cached__`, `__loader__`, and `__package__` is now deprecated. Consult [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) for alternatives.

[Subject index](INDEX.md) · [Previous](locating-and-executing-python-modules.md) · [Continue](runpy-run-path.md)
