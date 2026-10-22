# faulthandler — Dumping the C stack

### Dumping the C stack

Added in version 3.14.

 faulthandler.dump_c_stack(*file=sys.stderr*)

Write the C stack trace for the active thread to *file*.

When the Python build lacks support for it, or when the operating system supplies no stack trace, an error message is printed rather than a dumped C stack.

[Subject index](INDEX.md) · [Previous](faulthandler-dump-traceback.md) · [Continue](c-stack-compatibility.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
