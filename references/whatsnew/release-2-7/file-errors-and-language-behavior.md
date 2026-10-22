# Python 2.7 changes: File error reporting and core language behavior

On POSIX systems, the `file` object now populates the `filename` attribute of the [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) it raises when something tries to open a directory (a behavior Jan Kaliszewski pointed out; [bpo-4764](https://bugs.python.org/issue?@action=redirect&bpo=4764)), and it now tests up front for writes to a read-only file object and refuses them outright rather than relying on the C library to notice and flag the problem (corrected by Stefan Krah; [bpo-5677](https://bugs.python.org/issue?@action=redirect&bpo=5677)).

- Line endings are now normalized by the Python tokenizer on its own, which means the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in function will take source written with any line-ending convention. On top of that, the source no longer has to finish with a newline.

- Python 3.x rejects superfluous parentheses around function arguments, so `def f((x)): pass` is a syntax error there. Run with Python3 warnings turned on, Python 2.7 will now flag this peculiar form. (Pointed out by James Lingard; [bpo-7362](https://bugs.python.org/issue?@action=redirect&bpo=7362).)

- Weak references to old-style class objects can now be made. New-style classes have always permitted weak references. (Corrected by Antoine Pitrou; [bpo-8268](https://bugs.python.org/issue?@action=redirect&bpo=8268).)

- When a module object is collected by the garbage collector, the module's dictionary is now wiped only if nobody else still holds a reference to it ([bpo-7140](https://bugs.python.org/issue?@action=redirect&bpo=7140)).

[Subject index](INDEX.md) · [Previous source section](numeric-precision-and-format-field-changes.md) · [Next source section](interpreter-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](core-language-changes.md)
