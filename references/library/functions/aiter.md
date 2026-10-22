# aiter

aiter(*async_iterable*, */*)

Produce an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) for the supplied [asynchronous iterable](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterable). This amounts to invoking `x.__aiter__()`.

Note: In contrast to `iter()`, there is no 2-argument form of `aiter()`.

Added in version 3.10.

[Builtin task index](INDEX.md).
