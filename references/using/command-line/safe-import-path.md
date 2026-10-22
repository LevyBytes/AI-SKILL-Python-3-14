# -P

-P

Refrain from prepending a possibly unsafe path to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path):

- `python -m module` command line: Don't prepend the current working directory.

- `python script.py` command line: Don't prepend the script's directory. Should it be a symbolic link, resolve symbolic links.

- `python -c code` and `python` (REPL) command lines: Don't prepend an empty string, which stands for the current working directory.

See also the `PYTHONSAFEPATH` environment variable, and `-E` and `-I` (isolated) options.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source section](remove-docstrings.md) · [Following source section](quiet-startup.md)
