# pdb: `pdb.run()`

### Command-line interface

Debugging separate scripts is also possible by launching `pdb` from a shell. As an illustration:

```python
python -m pdb [-c command] (-m module | -p pid | pyfile) [args ...]

```

Run as a module, pdb starts post-mortem debugging by itself whenever the target program terminates with an error. Once post-mortem debugging finishes (or the program ends normally), pdb relaunches the program. This automatic relaunch keeps pdb's state intact (breakpoints included) and is usually preferable to leaving the debugger when the program ends.

 -c, --command &lt;command&gt;

Runs commands just as though they came from a `.pdbrc` file; see Debugger commands.

Changed in version 3.2: Added the `-c` option.

 -m &lt;module&gt;

Runs modules in much the way `python -m` does. Just like with a script, the debugger halts execution right before the module's first line.

Changed in version 3.7: Added the `-m` option.

 -p, --pid &lt;pid&gt;

Attach to the process with the specified PID.

Added in version 3.14.

For remote debugging of a live Python process, pass the `-p` or `--pid` option together with the PID of the process you want:

```python
python -m pdb -p 1234

```

Note

When a process is blocked inside a system call or waiting on I/O, attaching to it takes effect only after the next bytecode instruction runs or a signal arrives.

A statement can be run under the debugger's supervision in the following typical manner:

```python
>>> import pdb
>>> def f(x):
...     print(1 / x)
>>> pdb.run("f(2)")
> <string>(1)<module>()
(Pdb) continue
0.5
>>>

```

A program that has crashed is commonly examined like so:

```python
>>> import pdb
>>> def f(x):
...     print(1 / x)
...
>>> f(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
ZeroDivisionError: division by zero
>>> pdb.pm()
> <stdin>(2)f()
(Pdb) p x
0
(Pdb)

```

Changed in version 3.13: Because of the [**PEP 667**](https://peps.python.org/pep-0667/) implementation, names assigned through `pdb` now take effect right away in the live scope, including when execution runs within an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope).

These are the functions defined by the module; each one enters the debugger by a slightly different route:

 pdb.run(*statement*, *globals=None*, *locals=None*)

Run the *statement* (supplied as a string or a code object) with the debugger in control. The prompt shows up before any code runs; you may set breakpoints and enter `continue`, or advance through the statement with `step` or `next` (each of these commands is described further down). The optional *globals* and *locals* arguments define the environment for execution; the default is the dictionary of the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module. (See the discussion of the built-in [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) or [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) functions.)

[Subject index](INDEX.md) · [Previous](pdb-the-python-debugger.md) · [Continue](pdb-runeval-to-pdb-get-default-backend.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md)
