# faulthandler - C Stack Compatibility

### C Stack Compatibility

When the system lacks the C-level *[backtrace(3)](https://manpages.debian.org/backtrace(3))* or *[dladdr1(3)](https://manpages.debian.org/dladdr1(3))*, C stack dumps cannot function. The stack is replaced by a printed error.

On top of that, certain compilers lack support for [CPython’s](https://docs.python.org/3.14/glossary.html#term-CPython) approach to C stack dumps. Consequently, a different error might appear in place of the stack, even when the operating system can dump stacks.

Note

C stack dumps may take an unbounded amount of time, governed by the DWARF level of the binaries throughout the call stack.

[Subject index](INDEX.md) · [Previous](faulthandler-dump-c-stack.md) · [Continue](faulthandler-enable-to-faulthandler-is-enabled.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
