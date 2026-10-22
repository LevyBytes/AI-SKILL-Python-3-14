# Runtime and execution

Open when checking Python definitions for runtime and execution.

## CPython

The reference implementation of the Python programming language, the one handed out at [python.org](https://www.python.org). The label "CPython" comes into play when it is necessary to set this implementation apart from others, for instance Jython or IronPython.

## interpreted

Python falls into the interpreted camp rather than the compiled one, though the line can be hazy given that a bytecode compiler is involved. What this means is that source files run straight away, with no need to first build an executable explicitly and then run it. Compared with compiled languages, interpreted ones generally offer a quicker develop/debug loop, even if their programs usually run more slowly. See also interactive.

## virtual machine

A computer laid out wholly in software. Python's virtual machine runs the bytecode put out by the bytecode compiler.

## bytecode

Python source gets compiled down to bytecode, which is the in-memory form a Python program takes inside the CPython interpreter. That bytecode is additionally stashed in `.pyc` files, making a second run of the same file quicker (the recompile from source down to bytecode can be skipped). This "intermediate language" is described as running atop a virtual machine that carries out the machine code that matches each bytecode. Keep in mind that bytecodes are not meant to be portable across distinct Python virtual machines, nor to stay stable from one Python release to the next.

You can find the roster of bytecode instructions in the documentation for [the dis module](https://docs.python.org/3.14/library/dis.html#bytecodes).

## native code

Code compiled into machine instructions that runs straight on the processor, in contrast to code that is interpreted or executes inside a virtual machine. For Python, native code usually means C, C++, Rust or Fortran code residing in extension modules that Python can call. See also extension module.

## interpreter shutdown

Upon being told to stop, the Python interpreter moves into a distinct phase during which it progressively frees every allocated resource, including modules and assorted vital internal structures. It additionally invokes the garbage collector a number of times. Doing so can run code in user-defined destructors or weakref callbacks. Code that runs throughout the shutdown phase may meet various exceptions because the resources it depends on might no longer work (library modules or the warnings machinery being typical examples).

Interpreter shutdown chiefly happens because the `__main__` module, or the script being executed, has reached the end of its run.

## global state

Data reachable across an entire program, for example module-level variables, class variables, or C static variables within extension modules. Within multi-threaded programs, global state that threads share usually calls for synchronization so that race conditions and data races are prevented.

## interactive

Python supplies an interactive interpreter, which lets you key in statements and expressions at the interpreter prompt, run them on the spot, and view the outcome. Simply start `python` without any arguments (perhaps by picking it from your computer's main menu). It offers a highly effective means of trying out fresh ideas or examining modules and packages (keep `help(x)` in mind). To learn more about interactive mode, see [Interactive Mode](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac).

## interactive prompt

### Glossary

`>>>`

The prompt shown by default in Python's interactive shell. It appears frequently in code samples that you can run live inside the interpreter.

`...`

This may indicate either of the following:

- The prompt the interactive shell shows by default while you type the lines of an indented block, while you remain inside a matched pair of opening and closing delimiters (parentheses, square brackets, curly braces or triple quotes), or right after you write a decorator.

- The three dots form of the [Ellipsis](https://docs.python.org/3.14/library/stdtypes.html#bltin-ellipsis-object) object.

## REPL

A shorthand for the "read–eval–print loop", yet another label for the interactive interpreter shell.

## IDLE

An Integrated Development and Learning Environment for Python. [IDLE ? Python editor and shell](https://docs.python.org/3.14/library/idle.html#idle) is a modest editor-and-interpreter environment bundled with Python's standard distribution.

[Glossary context index](INDEX.md).
