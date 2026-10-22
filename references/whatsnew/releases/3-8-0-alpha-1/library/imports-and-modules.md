# Python 3.8.0 alpha 1 / library / imports and modules

[bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899): The Tokenize module now silently emits a NEWLINE whenever given input lacking a trailing new line. That conduct now mirrors what the C tokenizer performs internally. Contributed by Ammar Askar.

[bpo-31908](https://bugs.python.org/issue?@action=redirect&bpo=31908): Correct the cover-file output of the `trace` module's command-line tool. Formerly, cover files were written solely when the `--missing` option was given. Patch by Michael Selik.

[bpo-31787](https://bugs.python.org/issue?@action=redirect&bpo=31787): Corrected reference leaks coming from `__init__()` methods across several modules. (Contributed by Oren Milman)

[bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333): The `_abc` module joins the build. It is a speedup module carrying C implementations for assorted functions and methods in `abc`. Building an ABC subclass and invoking `isinstance` or `issubclass` against an ABC subclass run as much as 1.5x faster. On top of that, Python start-up gets up to 10% faster.

Note that this fresh implementation conceals the internal registry and caches that were formerly reachable through the private attributes `_abc_registry`, `_abc_cache`, and `_abc_negative_cache`. Three debugging helper methods are available in their place: `_dump_registry`, `_abc_registry_clear`, and `_abc_caches_clear`.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Small corrections across the typing module: annotations added to `NamedTuple.__new__`, and `*args` plus `**kwds` passed through in `Generic.__new__`. Original PRs by Paulius ??arka and Chad Dombrova.

[bpo-13312](https://bugs.python.org/issue?@action=redirect&bpo=13312): Heads off a potential integer underflow (undefined behavior) within the time module's year-handling code when a very low negative year value is passed.

[bpo-6700](https://bugs.python.org/issue?@action=redirect&bpo=6700): Corrected inspect.getsourcelines for module-level frames and tracebacks. Vladimir Matveev wrote the patch.

[bpo-35643](https://bugs.python.org/issue?@action=redirect&bpo=35643): Resolved a SyntaxWarning about an invalid escape sequence inside Modules/_sha3/cleanup.py. Patch by Mickaël Schoentgen.

[bpo-35471](https://bugs.python.org/issue?@action=redirect&bpo=35471): Python 2.4 ended MacOS 9 support. The macpath module had been deprecated back in Python 3.7. That module is now gone.

[bpo-22674](https://bugs.python.org/issue?@action=redirect&bpo=22674): Add the strsignal() function into the signal module, returning the system description of a given signal exactly as strsignal(3) returns it.

[bpo-35341](https://bugs.python.org/issue?@action=redirect&bpo=35341): Provide a generic flavor of `collections.OrderedDict` inside the `typing` module. Patch by Ismo Toijala.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
