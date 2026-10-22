# Python 3.11.0 alpha 7 / core and builtins / exceptions

[bpo-47212](https://bugs.python.org/issue?@action=redirect&bpo=47212): A bare `except` lacking any indented body that follows now triggers [`IndentationError`](https://docs.python.org/3.14/library/exceptions.html#IndentationError) rather than [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). The `SyntaxError` placement also got better for an un-parenthesized generator passed as arguments. Matthieu Dartiailh supplied the patch.

[bpo-46775](https://bugs.python.org/issue?@action=redirect&bpo=46775): Certain Windows system error codes(>= 10000) now translate to the proper errno and can raise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) subclass. Donghee Na contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
