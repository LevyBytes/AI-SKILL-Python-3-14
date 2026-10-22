# What's new in Python 3.14 / CPython bytecode changes — dis, string.templatelib

### CPython bytecode changes

- Swapped out the `BINARY_SUBSCR` opcode for the [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP) opcode carrying the `NB_SUBSCR` oparg. (Contributed by Irit Katriel in [gh-100239](https://github.com/python/cpython/issues/100239).)

- Introduce the [`BUILD_INTERPOLATION`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_INTERPOLATION) and [`BUILD_TEMPLATE`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_TEMPLATE) opcodes that build fresh [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) and [`Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) instances in turn. (Contributed by Lysandros Nikolaou together with others in [gh-132661](https://github.com/python/cpython/issues/132661); consult PEP 750 on template strings as well).

- Drop the `BUILD_CONST_KEY_MAP` opcode. Lean on [`BUILD_MAP`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_MAP) instead. (Contributed by Mark Shannon in [gh-122160](https://github.com/python/cpython/issues/122160).)

- Swap the `LOAD_ASSERTION_ERROR` opcode for [`LOAD_COMMON_CONSTANT`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_COMMON_CONSTANT), gaining the ability to load [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

- Introduce the [`LOAD_FAST_BORROW`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FAST_BORROW) and [`LOAD_FAST_BORROW_LOAD_FAST_BORROW`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_FAST_BORROW_LOAD_FAST_BORROW) opcodes that cut reference-counting cost whenever the interpreter can establish that the frame's reference outlasts the one pushed onto the stack. (Contributed by Matt Page in [gh-130704](https://github.com/python/cpython/issues/130704).)

- Introduce the [`LOAD_SMALL_INT`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SMALL_INT) opcode, which puts onto the stack a small integer matching the `oparg`. With it no longer needed, the `RETURN_CONST` opcode goes away. (Contributed by Mark Shannon in [gh-125837](https://github.com/python/cpython/issues/125837).)

- Introduce the fresh [`LOAD_SPECIAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SPECIAL) instruction. Emit code for [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statements by way of the new instruction. The `BEFORE_WITH` and `BEFORE_ASYNC_WITH` instructions were dropped. (Contributed by Mark Shannon in [gh-120507](https://github.com/python/cpython/issues/120507).)

- Introduce the [`POP_ITER`](https://docs.python.org/3.14/library/dis.html#opcode-POP_ITER) opcode that backs ?virtual? iterators. (Contributed by Mark Shannon in [gh-132554](https://github.com/python/cpython/issues/132554).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-future-versions-splituser.md) · [Next source section](pseudo-instructions.md) · [Release/subject declaration](summary-release-highlights.md)
