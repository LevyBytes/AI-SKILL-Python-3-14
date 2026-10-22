# faulthandler — Dumping the traceback

### Dumping the traceback

 faulthandler.dump_traceback(*file=sys.stderr*, *all_threads=True*)

Write the tracebacks for every thread to *file*. When *all_threads* is `False`, only the active thread is dumped.

See also

[`traceback.print_tb()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_tb), which can be used to print a traceback object.

Changed in version 3.5: A file descriptor may now be passed to this function.

[Subject index](INDEX.md) · [Previous](faulthandler-dump-the-python-traceback.md) · [Continue](faulthandler-dump-c-stack.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
