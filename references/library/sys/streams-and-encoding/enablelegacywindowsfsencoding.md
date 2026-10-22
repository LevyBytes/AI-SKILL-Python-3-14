# sys._enablelegacywindowsfsencoding

sys._enablelegacywindowsfsencoding()

Switches the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) over to ‘mbcs’ and ‘replace’ in turn, matching how Python behaved before 3.6.

Doing this amounts to setting the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable ahead of starting Python.

Refer as well to `sys.getfilesystemencoding()` and `sys.getfilesystemencodeerrors()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Note

Altering the filesystem encoding once Python is already up is hazardous, since the former fsencoding — or paths that were encoded with it — might sit cached somewhere. Lean on [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) in its place.

Added in version 3.6: See [**PEP 529**](https://peps.python.org/pep-0529/) for more details.

Deprecated since version 3.13, will be removed in version 3.16: Lean on [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) in its place.

[API family](INDEX.md) · [sys context index](../INDEX.md).
