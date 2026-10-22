# pdb: Debugger interactive interpreter and remaining commands

interact

Launch an interactive interpreter (built on the [`code`](https://docs.python.org/3.14/library/code.html#module-code) module) in a fresh global namespace seeded from the local and global namespaces of the current scope. Use `exit()` or `quit()` to leave the interpreter and go back to the debugger.

Note

Since `interact` builds a fresh, dedicated namespace for running code, assigning to variables there leaves the original namespaces untouched. Changes made to any referenced mutable objects, however, do show up in the original namespaces as usual.

Added in version 3.2.

Changed in version 3.13: You can leave the `interact` command with `exit()` or `quit()`.

Changed in version 3.13: `interact` now sends its output to the debugger's output channel instead of [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

 alias [name [command]]

Define an alias named *name* that runs *command*. Do *not* wrap the *command* in quotes. You can mark substitutable parameters with `%1`, `%2`, … through `%9`, while `%*` stands in for every parameter. When *command* is left off, the existing alias for *name* is displayed. When no arguments at all are supplied, every alias is listed.

retval

Show the value that the current function handed back on its most recent return.

 exceptions [excnumber]

Show the chained exceptions or hop from one to another.

If you call `pdb.pm()` or `Pdb.post_mortem(...)` against a chained exception rather than a traceback, you're able to navigate among those chained exceptions: run the `exceptions` command on its own to list them, and `exceptions <number>` to jump to the one you want.

Example:

```python
def out():
    try:
        middle()
    except Exception as e:
        raise ValueError("reraise middle() error") from e

def middle():
    try:
        return inner(0)
    except Exception as e:
        raise ValueError("Middle fail")

def inner(x):
    1 / x

 out()

```

invoking `pdb.pm()` lets you travel from one exception to another:

```python
> example.py(5)out()
-> raise ValueError("reraise middle() error") from e

(Pdb) exceptions
  0 ZeroDivisionError('division by zero')
  1 ValueError('Middle fail')
> 2 ValueError('reraise middle() error')

(Pdb) exceptions 0
> example.py(16)inner()
-> 1 / x

(Pdb) up
> example.py(10)middle()
-> return inner(0)

```

Added in version 3.13.

Footnotes

[Subject index](INDEX.md) · [Previous](a.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Debugger commands](debugger-commands-section-introduction-and-initial-examples.md) · [Required continuation of the source contract](pdb-alias-command.md) · [Previous](q.md)
