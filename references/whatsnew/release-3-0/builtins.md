# What's New In Python 3.0 / Builtins — functools, io, sys

### Builtins

- [**PEP 3135**](https://peps.python.org/pep-3135/): New [`super()`](https://docs.python.org/3.14/library/functions.html#super). It is now possible to call `super()` with no arguments at all, and (provided you are inside an ordinary instance method written within a [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) statement) the appropriate class and instance get picked for you. Supply arguments and `super()` works exactly as it always did.

- [**PEP 3111**](https://peps.python.org/pep-3111/): `raw_input()` now answers to [`input()`](https://docs.python.org/3.14/library/functions.html#input). In other words, the redefined `input()` pulls one line off [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and hands it back with the closing newline removed. Should input end too soon, it raises [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError). Want the former `input()` semantics? Then write `eval(input())`.

- A fresh built-in, [`next()`](https://docs.python.org/3.14/library/functions.html#next), was introduced so you can invoke an object's [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method.

- Both the rounding policy and the result type of the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function have shifted. A value sitting precisely halfway is now pushed toward the closest even outcome rather than rounded away from zero. (As an example, `round(2.5)` yields `2` these days in place of `3`.) Rather than invariably handing back a float, `round(x[, n])` now hands the work off to `x.__round__([n])`. Given one argument it usually produces an integer, and given two it produces a value matching the type of `x`.

- Moved `intern()` to [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern).

- Dropped: `apply()`. Where you would have written `apply(f, args)`, write `f(*args)`.

- Dropped [`callable()`](https://docs.python.org/3.14/library/functions.html#callable). In place of `callable(f)` you may write `isinstance(f, collections.Callable)`. The `operator.isCallable()` function has been removed as well.

- Dropped `coerce()`. With old-style classes out of the picture, the function has nothing left to do.

- Dropped `execfile()`. Swap `execfile(fn)` for `exec(open(fn).read())`.

- Dropped the `file` type. Reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open) instead. These days open is capable of returning several distinct stream varieties drawn from the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module.

- Dropped `reduce()`. Should you truly require it, [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) is there; for some 99 percent of cases, though, a spelled-out [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop reads more clearly.

- Removed `reload()`. Use `imp.reload()`.

- Removed. `dict.has_key()` – use the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator instead.

[Subject index](INDEX.md) · [Previous source section](operators-and-special-methods.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](common-stumbling-blocks.md)
