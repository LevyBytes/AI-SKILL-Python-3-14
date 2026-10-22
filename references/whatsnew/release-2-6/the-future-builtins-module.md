# What’s New in Python 2.6 / The `future_builtins` module

### The `future_builtins` module

The roster of built-in functions is reworked heavily in Python 3.0, and most of those revisions cannot land in the Python 2.x line because doing so would break compatibility. As a bridge, the `future_builtins` module offers variants of these built-ins that you can import while authoring code meant to run under 3.0.

At present the module exposes the following functions:

- `ascii(obj)`: equivalent to [`repr()`](https://docs.python.org/3.14/library/functions.html#repr). Under Python 3.0, `repr()` hands back a Unicode string, whereas [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii) yields a pure ASCII bytestring.

- `filter(predicate, iterable)`, `map(func, iterable1, ...)`: the 3.0 editions hand back iterators, in contrast to the 2.x built-ins, which hand back lists.

- `hex(value)`, `oct(value)`: rather than invoking the `__hex__()` or `__oct__()` methods, these editions invoke the `__index__()` method and turn the outcome into hexadecimal or octal. [`oct()`](https://docs.python.org/3.14/library/functions.html#oct) emits its result with the new `0o` notation.

[Subject index](INDEX.md) · [Previous source section](the-ast-module.md) · [Next source section](the-json-module-javascript-object-notation.md) · [Release/subject declaration](python-3-0.md)
