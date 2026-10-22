# How do I create a .pyc file?

### Modules

### How do I create a .pyc file?

The very first time a module gets imported — or whenever its source has been edited since the existing bytecode was built — the interpreter is supposed to produce a `.pyc` file holding the compiled form inside a `__pycache__` subdirectory located next to the `.py` file. That `.pyc` file keeps the original `.py` file's base name, finishes with the `.pyc` suffix, and carries a middle segment tied to the specific `python` binary that produced it. (Consult [**PEP 3147**](https://peps.python.org/pep-3147/) for the full account.)

A frequent reason a `.pyc` file fails to appear is that the folder holding the source lacks permission to make the `__pycache__` subdirectory. You might hit this, say, when your development account differs from the one the program runs under — a typical situation while testing behind a web server.

So long as the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable stays unset, the `.pyc` file is written automatically whenever you import a module and Python is able (sufficient permissions, free disk space, and so forth) to make a `__pycache__` subdirectory and store the compiled module inside it.

Launching Python against a top-level script counts as an execution and not an import, so nothing in `.pyc` form results. Imagine a top-level module `foo.py` that pulls in another module `xyz.py`: starting `foo` (by entering `python foo.py` at the shell) yields a `.pyc` for `xyz`, since `xyz` was imported, yet no `.pyc` file is built for `foo` because `foo.py` itself never got imported.

Should you still want a `.pyc` for `foo` — that is, to produce one for a module nobody imports — you can do so with the [`py_compile`](https://docs.python.org/3.14/library/py_compile.html#module-py_compile) and [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) modules.

Any module can be compiled by hand through the [`py_compile`](https://docs.python.org/3.14/library/py_compile.html#module-py_compile) module. A convenient route is to call its `compile()` function from an interactive session:

```python
>>> import py_compile
>>> py_compile.compile('foo.py')

```

That places the `.pyc` into a `__pycache__` subdirectory sitting beside `foo.py` (though the optional parameter *cfile* lets you send it elsewhere).

There is also a way to compile every file across one or more directories at once, by way of the [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) module. Run `compileall.py` from the shell prompt and hand it the path to a directory full of Python files you want compiled:

```python
python -m compileall .

```

[Subject index](INDEX.md)
