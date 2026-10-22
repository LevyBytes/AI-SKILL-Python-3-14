# -m &lt;module-name&gt;

-m &lt;module-name&gt;

Resolve the module through the ordinary import machinery and run what it contains as the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module.

Because the argument names a *module*, omit any file extension (`.py`). Although the module name ought to be a valid absolute Python module name, the implementation does not necessarily check this in every case (for instance, it might let a hyphen appear in the name).

You may also pass package names, namespace packages included. Hand the interpreter a package name rather than an ordinary module and it runs `<pkg>.__main__` as the principal module. This is intentionally consistent with how directories and zipfiles given to the interpreter as the script argument get treated.

Note

Built-in modules and C-coded extension modules can't be targeted with this option, because they lack Python module files. That said, it still works for precompiled modules, even where the original source file has gone missing.

When you supply this option, [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) begins with the complete path to the module file (during the search for that file, the initial entry is temporarily `"-m"`). Just like the `-c` option, the current directory gets inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

The `-I` option lets you run the script in isolated mode, where [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) includes neither the current directory nor the user's site-packages directory. Every `PYTHON*` environment variable is disregarded as well.

A good number of standard library modules ship with code that runs whenever they are executed as a script. Take the [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module as one such case:

```sh
python -m timeit -s "setup here" "benchmarked code here"
python -m timeit -h # for details

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_module` with argument `module-name`.

See also

[`runpy.run_module()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_module)

Equivalent functionality directly available to Python code

[**PEP 338**](https://peps.python.org/pep-0338/) – Executing modules as scripts

Changed in version 3.1: Pass the package name to launch a `__main__` submodule.

Changed in version 3.4: namespace packages are also supported

[Subject index](INDEX.md) · [Previous source section](c-command.md) · [Following source section](read-python-source-from-standard-input.md)
