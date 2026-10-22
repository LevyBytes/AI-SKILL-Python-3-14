# What's New In Python 3.13 / traceback

### traceback

-

Introduce the [`exc_type_str`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.exc_type_str) attribute on [`TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException); it carries a string rendering of the *exc_type*. The [`exc_type`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.exc_type) attribute, which keeps the type object directly, is now deprecated. A *save_exc_type* parameter (defaulting to `True`) controls whether `exc_type` gets retained. (Contributed by Irit Katriel in [gh-112332](https://github.com/python/cpython/issues/112332).)

- A fresh *show_group* keyword-only parameter joins [`TracebackException.format_exception_only()`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.format_exception_only); it formats, recursively, the nested exceptions belonging to a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) instance. (Contributed by Irit Katriel in [gh-105292](https://github.com/python/cpython/issues/105292).)

[Subject index](INDEX.md) · [Previous source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](types.md)
