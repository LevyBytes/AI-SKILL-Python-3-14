# What’s New in Python 2.1 / PEP 235: Importing Modules on Case-Insensitive Platforms

### PEP 235: Importing Modules on Case-Insensitive Platforms

Certain operating systems carry filesystems that ignore case, with MacOS and Windows the chief examples; on those systems you can’t tell the filenames `FILE.PY` and `file.py` apart, even though the original case of the file’s name is retained (they preserve case as well).

In Python 2.1, the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement is rigged to emulate case-sensitivity on case-insensitive platforms. By default Python now hunts for the first case-sensitive match, raising an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) when no such file turns up, so `import file` won’t pull in a module called `FILE.PY`. You can ask for case-insensitive matching by setting the [`PYTHONCASEOK`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCASEOK) environment variable ahead of launching the Python interpreter.

[Subject index](INDEX.md) · [Previous source section](pep-232-function-attributes.md) · [Next source section](pep-217-interactive-display-hook.md) · [Release/subject declaration](introduction.md)
