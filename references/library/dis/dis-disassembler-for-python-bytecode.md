# dis — `dis` — Disassembler for Python bytecode

### `dis` — Disassembler for Python bytecode

**Source code:** [Lib/dis.py](https://github.com/python/cpython/tree/3.14/Lib/dis.py)

---

By disassembling it, the `dis` module makes CPython [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) available for inspection. That input bytecode for CPython, which this module consumes, is declared inside `Include/opcode.h` and is what the compiler and interpreter rely on.

**CPython implementation detail:** Within the CPython interpreter, bytecode is an internal detail. There is no promise that opcodes won't be introduced, dropped, or altered from one Python release to the next. You should therefore not treat this module as portable across differing Python VMs or differing Python versions.

Changed in version 3.6: Each instruction occupies 2 bytes now. Formerly, the byte count differed from one instruction to another.

Changed in version 3.10: For jump, exception-handling, and loop instructions, the argument has become the instruction offset in place of the byte offset.

Changed in version 3.11: Certain instructions now carry one or several inline cache entries alongside them, expressed as `CACHE` instructions. By default they stay hidden, yet supplying `show_caches=True` to any `dis` utility reveals them. On top of that, the interpreter today reshapes the bytecode to specialize it according to varying runtime conditions. Supplying `adaptive=True` surfaces that adaptive bytecode.

Changed in version 3.12: A jump's argument now gives the target instruction's offset measured relative to whatever instruction follows directly after the jump instruction's `CACHE` entries.

The upshot is that the `CACHE` instructions stay invisible where forward jumps are concerned, though they must be factored in whenever you reason about backward jumps.

Changed in version 3.13: For jump targets and exception handlers, the output now prints logical labels in place of instruction offsets. Both the `-O` command line option and the `show_offsets` argument arrived here.

Changed in version 3.14: This release introduced the `-P` command-line option together with the `show_positions` argument.

The `-S` command-line option is added.

Example: Given the function `myfunc()`:

```python
def myfunc(alist):
    return len(alist)

```

the disassembly of `myfunc()` can be shown by running the command below:

```pycon
>>> dis.dis(myfunc)
  2           RESUME                   0

  3           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (alist)
              CALL                     1
              RETURN_VALUE

```

(The “2” is a line number).

[Subject index](INDEX.md) · [Continue](command-line-interface.md)
