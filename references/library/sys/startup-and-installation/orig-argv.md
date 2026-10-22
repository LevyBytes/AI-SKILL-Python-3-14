# sys.orig_argv

sys.orig_argv

The list of the original command line arguments handed to the Python executable.

The members of `sys.orig_argv` are the arguments aimed at the Python interpreter, whereas the members of `sys.argv` are the arguments aimed at the user’s program. Arguments that the interpreter itself consumes show up in `sys.orig_argv` and are absent from `sys.argv`.

Added in version 3.10.

[API family](INDEX.md) · [sys context index](../INDEX.md).
