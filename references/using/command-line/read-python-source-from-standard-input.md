# Read Python source from standard input

- Take commands from standard input ([`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin)). When standard input happens to be a terminal, `-i` is implied.

When you supply this option, [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) begins with `"-"`, and the current directory is inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_stdin` with no arguments.

[Subject index](INDEX.md) · [Previous source section](m-module-name.md) · [Following source section](run-a-python-file-directory-or-zip-archive.md)
