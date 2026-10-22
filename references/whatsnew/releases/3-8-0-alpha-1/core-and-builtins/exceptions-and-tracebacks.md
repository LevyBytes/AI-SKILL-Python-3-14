# Python 3.8.0 alpha 1 / core and builtins / exceptions and tracebacks

[bpo-17288](https://bugs.python.org/issue?@action=redirect&bpo=17288): Block jumps originating from ?return? and ?exception? trace events.

[bpo-32932](https://bugs.python.org/issue?@action=redirect&bpo=32932): Make the error message clearer whenever `__all__` holds objects that are not str.

[bpo-12458](https://bugs.python.org/issue?@action=redirect&bpo=12458): Tracebacks now report the right line number for subexpressions inside multiline expressions. For multiline expressions, tracebacks now report the line number of the first line rather than that of the final subexpression.

[bpo-33138](https://bugs.python.org/issue?@action=redirect&bpo=33138): Revised the standard error message for non-pickleable and non-copyable types. It now reads ?cannot pickle? rather than ?can't pickle? or ?cannot serialize?.

[bpo-10544](https://bugs.python.org/issue?@action=redirect&bpo=10544): Within comprehensions and generator expressions, yield expressions are no longer permitted, with the lone exception of the expression supplying the outermost iterable.

[bpo-35713](https://bugs.python.org/issue?@action=redirect&bpo=35713): Restructure Python initialization to bring working exceptions and sys.stderr online sooner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
