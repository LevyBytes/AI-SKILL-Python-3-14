# pdb — `pdb` — The Python Debugger

### `pdb` — The Python Debugger

**Source code:** [Lib/pdb.py](https://github.com/python/cpython/tree/3.14/Lib/pdb.py)

---

An interactive source-level debugger for Python programs is what the `pdb` module provides. Among its capabilities are placing (conditional) breakpoints, stepping a single line at a time, examining stack frames, listing source, and running arbitrary Python expressions within the scope of any frame. Post-mortem debugging is supported too, and the debugger can be driven programmatically.

You can extend the debugger, since it is implemented as the `Pdb` class. That class is presently undocumented, though reading the source makes it straightforward to follow. Its extension surface builds on the [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) and [`cmd`](https://docs.python.org/3.14/library/cmd.html#module-cmd) modules.

See also

Module [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler)

Lets you dump Python tracebacks deliberately: on a fault, once a timeout elapses, or upon a user signal.

Module [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback)

The standard way to pull out, format, and print the stack traces of Python programs.

To drop into the debugger, the common approach is to add:

```python
import pdb; pdb.set_trace()

```

Or:

```python
breakpoint()

```

wherever you want execution to halt, and then launch the program. From there you can walk through the statements that follow, and resume normal execution outside the debugger with the `continue` command.

Changed in version 3.7: With its default arguments, the built-in [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) serves as a replacement for `import pdb; pdb.set_trace()`.

```python
def double(x):
   breakpoint()
   return x * 2
val = 3
print(f"{val} * 2 is {double(val)}")

```

Once in debug mode, the debugger shows the prompt `(Pdb)`, signaling that the session is active:

```python
> ...(2)double()
-> breakpoint()
(Pdb) p x
3
(Pdb) continue
3 * 2 is 6

```

Changed in version 3.3: The [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module supplies Tab-completion for both commands and their arguments; for instance, the live global and local names show up as candidate arguments to the `p` command.

[Subject index](INDEX.md) · [Continue](pdb-run.md)
