# -c &lt;command&gt;

-c &lt;command&gt;

Run the Python source contained in *command*. Multiple statements may make up *command*, divided by newlines, and leading whitespace matters just as it does in ordinary module code.

When you supply this option, [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) begins with `"-c"`, and the current directory is inserted at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) (so that modules sitting there can be imported as top level modules).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_command` with argument `command`.

Changed in version 3.14: *command* is automatically dedented before execution.

[Subject index](INDEX.md) · [Previous source section](interface-options.md) · [Following source section](m-module-name.md)
