# Built-in Functions

breakpoint(**args*, ***kws*)

Calling this lands you inside the debugger right where the call sits. Concretely, it invokes [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook) and forwards `args` and `kws` to it unchanged. Out of the box, `sys.breakpointhook()` invokes [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) with no arguments expected. Here it works purely as a shortcut, sparing you from having to import [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) explicitly or write out extra code to reach the debugger. That said, you can point `sys.breakpointhook()` at a different function, and `breakpoint()` will then invoke that one automatically, letting you reach whichever debugger you prefer. When `sys.breakpointhook()` cannot be reached, this function raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Out of the box, you can adjust how `breakpoint()` behaves through the [`PYTHONBREAKPOINT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONBREAKPOINT) environment variable. Consult [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook) for the usage particulars.

Bear in mind that this no longer holds once [`sys.breakpointhook()`](https://docs.python.org/3.14/library/sys.html#sys.breakpointhook) has been swapped out.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `builtins.breakpoint` with argument `breakpointhook`.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](bool-class.md) · [Continue](bytearray-class-to-bytearray-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
