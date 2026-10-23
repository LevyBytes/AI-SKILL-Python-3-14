# What's New In Python 3.7 / warnings - sys

### warnings

How the default warnings filters get set up has been revised in these ways:

- warnings switched on through command line options (among them those for [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) and the freshly added CPython-specific [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `dev` option) always reach the warnings machinery by way of the [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) attribute.

- warnings filters turned on through the command line or through the environment now follow this precedence ordering:

  - the `BytesWarning` filter for [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) (or `-bb`)

  - any filters specified with the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) option

  - any filters specified with the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable

  - any other CPython specific filters (e.g. the `default` filter added for the new `-X dev` mode)

  - any implicit filters defined directly by the warnings machinery

- within [CPython debug builds](https://docs.python.org/3.14/using/configure.html#debug-build), every warning is now shown by default (the implicit filter list holds nothing)

(Contributed by Nick Coghlan and Victor Stinner in [bpo-20361](https://bugs.python.org/issue?@action=redirect&bpo=20361), [bpo-32043](https://bugs.python.org/issue?@action=redirect&bpo=32043), and [bpo-32230](https://bugs.python.org/issue?@action=redirect&bpo=32230).)

At the interactive prompt and within single-file scripts, deprecation warnings are again surfaced by default. Consult PEP 565: Show DeprecationWarning in __main__ for the specifics. (Contributed by Nick Coghlan in [bpo-31975](https://bugs.python.org/issue?@action=redirect&bpo=31975).)

[Subject index](INDEX.md) · [Previous source section](uuid.md) · [Next source section](xml.md) · [Release/subject declaration](summary-release-highlights.md)
