# dis.Positions: `COPY_FREE_VARS()`, `RAISE_VARARGS()`, `CALL()`, `CALL_KW()`, `CALL_FUNCTION_EX()`

COPY_FREE_VARS(*n*)

Copies the `n` [free (closure) variables](https://docs.python.org/3.14/glossary.html#term-closure-variable) out of the closure into the frame. This removes the need for any special handling on the caller's side while invoking closures.

Added in version 3.11.

 RAISE_VARARGS(*argc*)

Throws an exception via one of the 3 forms of the `raise` statement, according to the value of *argc*:

- 0: `raise` (re-raise previous exception)

- 1: `raise STACK[-1]` (raise exception instance or type at `STACK[-1]`)

- 2: `raise STACK[-2] from STACK[-1]` (raise exception instance or type at `STACK[-2]` with `__cause__` set to `STACK[-1]`)

 CALL(*argc*)

Invokes a callable object using the number of arguments given by `argc`. The stack holds (in ascending order):

- The callable

- `self` or `NULL`

- The remaining positional arguments

Here `argc` counts the positional arguments, leaving out `self`.

`CALL` removes every argument and the callable object from the stack, invokes the callable object with those arguments, and places the value the callable object returned onto the stack.

Added in version 3.11.

Changed in version 3.13: The callable now consistently sits at the same stack position.

Changed in version 3.13: Calls carrying keyword arguments are now processed by `CALL_KW`.

 CALL_KW(*argc*)

Invokes a callable object using the number of arguments given by `argc`, which includes one or more named arguments. The stack holds (in ascending order):

- The callable

- `self` or `NULL`

- The remaining positional arguments

- The named arguments

- A [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) of keyword argument names

Here `argc` counts the positional and named arguments together, leaving out `self`. The length of the keyword argument names tuple equals the number of named arguments.

`CALL_KW` removes every argument, the keyword names, and the callable object from the stack, invokes the callable object with those arguments, and places the value the callable object returned onto the stack.

Added in version 3.13.

 CALL_FUNCTION_EX(*flags*)

Invokes a callable object with a variable collection of positional and keyword arguments. When the lowest bit of *flags* is set, the top of the stack holds a mapping object carrying extra keyword arguments. Ahead of the callable being invoked, both the mapping object and the iterable object are ?unpacked? and their contents are supplied as keyword and positional arguments respectively. `CALL_FUNCTION_EX` removes every argument and the callable object from the stack, invokes the callable object with those arguments, and places the value the callable object returned onto the stack.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](dis-positions-load-fast-borrow-to-dis-positions-delete-deref.md) · [Continue](bytecode-function-attributes-and-argument-extension.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
