# 6.1.2. The Module Search Path

### 6.1.2. The Module Search Path

When a module called `spam` is imported, the interpreter starts by hunting for a built-in module of that name. Such module names appear in [`sys.builtin_module_names`](https://docs.python.org/3.14/library/sys.html#sys.builtin_module_names). Failing that, it goes looking for a file `spam.py` across a set of directories named by the variable [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). `sys.path` gets its starting values from these spots:

- The directory holding the input script (or the current directory when nothing is specified).

- [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names that follows the same syntax as the shell variable `PATH`).

- The installation-dependent default (which by convention includes a `site-packages` directory, managed by the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module).

Further details live at [The initialization of the sys.path module search path](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init).

Note

On file systems that support symlinks, the directory holding the input script is worked out only after the symlink has been resolved. Put another way, the directory holding the symlink is **not** placed on the module search path.

Once initialization is done, Python programs are free to alter [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). The directory of the script currently running goes at the front of the search path, in front of the standard library path. So scripts in that directory are picked up rather than library-directory modules sharing the same name. Unless you meant to make that swap, it's a mistake. Refer to the Standard Modules section for additional details.

[Subject index](INDEX.md) · [Previous source section](executing-modules-as-scripts.md) · [Following source section](compiled-python-files.md)
