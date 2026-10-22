# What’s New in Python 2.7 / Changes to the Handling of Deprecation Warnings

### Changes to the Handling of Deprecation Warnings

In Python 2.7, a policy choice was made so that warnings of concern only to developers are silenced by default. [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) along with its subclasses are now disregarded unless specifically requested, which keeps users from encountering warnings raised by an application. The same change went into the branch that became Python 3.2. (Debated on stdlib-sig and implemented in [bpo-7319](https://bugs.python.org/issue?@action=redirect&bpo=7319).)

In earlier releases, [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) messages appeared by default, giving Python developers a plain signal of the places where their code might fail in some future major Python version.

Yet there are ever more people running Python-based applications who play no direct role in developing those applications. To such users the [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) messages mean nothing, causing them to fret over an application that is in fact functioning fine while loading application developers down with answering those worries.

To turn the display of [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) messages back on, run Python with the [`-Wdefault`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) (abbreviated as `-Wd`) switch, or set the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable to `"default"` (or `"d"`) prior to starting Python. From within Python code, a call to `warnings.simplefilter('default')` likewise restores them.

When it runs tests, the `unittest` module also turns deprecation warnings back on automatically.

[Subject index](INDEX.md) · [Previous source section](the-future-for-python-2-x.md) · [Next source section](python-3-1-features.md) · [Release/subject declaration](the-future-for-python-2-x.md)
