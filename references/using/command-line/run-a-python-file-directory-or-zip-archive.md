# Run a Python file, directory or zip archive

Run the Python source held in *script*, which has to be a filesystem path (whether absolute or relative) pointing to a Python file, a directory holding a `__main__.py` file, or a zipfile holding a `__main__.py` file.

When you supply this option, the initial entry of [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) is the script name exactly as it appeared on the command line.

Where the script name points straight at a Python file, that file's containing directory is inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), and the file runs as the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module.

Where the script name points at a directory or zipfile instead, the script name itself is inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), and the `__main__.py` file located there runs as the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module.

The `-I` option lets you run the script in isolated mode, where [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) includes neither the script's directory nor the user's site-packages directory. Every `PYTHON*` environment variable is disregarded as well.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_file` with argument `filename`.

See also

[`runpy.run_path()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_path)

Equivalent functionality directly available to Python code

[Subject index](INDEX.md) · [Previous source section](read-python-source-from-standard-input.md) · [Following source section](interactive-defaults-without-an-interface-option.md)
