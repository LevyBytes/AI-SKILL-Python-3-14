# Python 3.14.0 alpha 1 / core and builtins / exceptions

[gh-123123](https://github.com/python/cpython/issues/123123): Correct the rendering of [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions that span several lines. Pablo Galindo authored this.

[gh-119933](https://github.com/python/cpython/issues/119933): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) messages whenever an invalid expression shows up within one of these spots: a type parameters bound, the constraint tuple of a type parameter, or a default for a type parameter. Bénédikt Tran contributed the fix.

[gh-123562](https://github.com/python/cpython/issues/123562): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) text emitted when `case ... as ...` is given something other than a name.

[gh-123446](https://github.com/python/cpython/issues/123446): Stop producing an empty function name in the [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) raised when builtin magic methods run without the arguments they require.

[gh-123440](https://github.com/python/cpython/issues/123440): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) text emitted when `except as` is given something other than a name.

[gh-121804](https://github.com/python/cpython/issues/121804): Display the right error positions whenever a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) surfaces in the basic REPL. Sergey B Kirpichev contributed the fix.

[gh-121657](https://github.com/python/cpython/issues/121657): Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) message produced when somebody uses [`yield from`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) outside a function.

[gh-121297](https://github.com/python/cpython/issues/121297): In the past, misusing [`await`](https://docs.python.org/3.14/reference/expressions.html#await) or asynchronous comprehensions inside code stripped out by the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) option went unflagged by the Python compiler. From now on such code raises [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Jelle Zijlstra contributed the fix.

[gh-121288](https://github.com/python/cpython/issues/121288): The [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) text from [`list.index()`](https://docs.python.org/3.14/library/stdtypes.html#list.index), [`range.index()`](https://docs.python.org/3.14/library/stdtypes.html#range.index), `deque.index()`, `deque.remove()` and `ShareableList.index()` no longer embeds the repr of the value being searched for (which may be arbitrarily large) and now lines up with the error messages from the other [`index()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.index) and [`remove()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.remove) methods.

[gh-118692](https://github.com/python/cpython/issues/118692): Skip the needless creation of [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) instances during monitoring.

[gh-119057](https://github.com/python/cpython/issues/119057): Better [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError) error text. Every message is now consistent: the `/`, `//`, and `%` operations all report ?division by zero?. Meanwhile `0 ** -1` reports ?zero to a negative power?.

[gh-123378](https://github.com/python/cpython/issues/123378): A crash in the [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) method of [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) objects, occurring when the [`UnicodeError.start`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.start) and [`UnicodeError.end`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.end) values are invalid or out of range, is fixed. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
