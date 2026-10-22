# traceback.TracebackException: `format()`, `format_exception_only()`

format(***, *chain=True*)

Format the exception.

Whenever *chain* is not `True`, `__cause__` and `__context__` go unformatted.

What this returns is a generator of strings, each closing with a newline and some carrying newlines inside them. `print_exception()` simply wraps this method, sending its lines to a file.

 format_exception_only(***, *show_group=False*)

Format the exception part of the traceback.

What this returns is a generator of strings, each closing with a newline.

When *show_group* is `False`, the generator yields the exception's message and then its notes (whenever there are any). That exception message is usually one string; for [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions, though, it runs across multiple lines that lay out (once printed) precise detail about where the syntax error happened.

Should *show_group* be `True` while the exception is itself a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup), the exceptions nested inside are likewise pulled in, walked recursively, and indented in keeping with their depth of nesting.

Changed in version 3.11: The exception's [`notes`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__notes__) now appear within the produced output.

Changed in version 3.13: Added the *show_group* parameter.

[Subject index](INDEX.md) · [Previous](traceback-tracebackexception-print.md) · [Continue](traceback-stacksummary-class.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Owning module, declaration or section: traceback.TracebackException](traceback-tracebackexception-class.md) · [Owning module, declaration or section: `TracebackException` Objects](traceback-tracebackexception-class.md)
