# What's New In Python 3.11 / inspect — inspect, types

### inspect

- [`getmembers_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmembers_static) was added; it yields every member without setting off dynamic resolution through the descriptor protocol. (Contributed by Weipeng Hong in [bpo-30533](https://bugs.python.org/issue?@action=redirect&bpo=30533).)

- [`ismethodwrapper()`](https://docs.python.org/3.14/library/inspect.html#inspect.ismethodwrapper) was added to test whether an object's type is a [`MethodWrapperType`](https://docs.python.org/3.14/library/types.html#types.MethodWrapperType). (Contributed by Hakan Çelik in [bpo-29418](https://bugs.python.org/issue?@action=redirect&bpo=29418).)

- The frame-oriented functions within the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module were changed to hand back fresh [`FrameInfo`](https://docs.python.org/3.14/library/inspect.html#inspect.FrameInfo) and [`Traceback`](https://docs.python.org/3.14/library/inspect.html#inspect.Traceback) class instances (still compatible with the earlier [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple)-style interfaces) that bundle the richer [**PEP 657**](https://peps.python.org/pep-0657/) position data (end line number, column and end column). These are the functions involved:

  - [`inspect.getframeinfo()`](https://docs.python.org/3.14/library/inspect.html#inspect.getframeinfo)

  - [`inspect.getouterframes()`](https://docs.python.org/3.14/library/inspect.html#inspect.getouterframes)

  - [`inspect.getinnerframes()`](https://docs.python.org/3.14/library/inspect.html#inspect.getinnerframes),

  - [`inspect.stack()`](https://docs.python.org/3.14/library/inspect.html#inspect.stack)

  - [`inspect.trace()`](https://docs.python.org/3.14/library/inspect.html#inspect.trace)

(Contributed by Pablo Galindo in [gh-88116](https://github.com/python/cpython/issues/88116).)

[Subject index](INDEX.md) · [Previous source section](idle-and-idlelib.md) · [Next source section](locale.md) · [Release/subject declaration](summary-release-highlights.md)
