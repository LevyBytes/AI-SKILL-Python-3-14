# PYTHONLEGACYWINDOWSFSENCODING

PYTHONLEGACYWINDOWSFSENCODING

When set to a non-empty string, the default [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) mode reverts to its pre-3.6 values of 'mbcs' and 'replace', respectively. If not, the new defaults 'utf-8' and 'surrogatepass' apply.

This may also be enabled at runtime with [`sys._enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.6: See [**PEP 529**](https://peps.python.org/pep-0529/) for more details.

[Subject index](INDEX.md) · [Previous source section](pythonmallocstats.md) · [Following source section](pythonlegacywindowsstdio.md)
