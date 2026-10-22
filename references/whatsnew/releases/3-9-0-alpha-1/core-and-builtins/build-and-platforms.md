# Python 3.9.0 alpha 1 / core and builtins / build and platforms

[bpo-20523](https://bugs.python.org/issue?@action=redirect&bpo=20523): `pdb.Pdb` honours ~/.pdbrc on Windows 7. Tim Hopper together with Dan Lidral-Porter contributed the patch.

[bpo-37830](https://bugs.python.org/issue?@action=redirect&bpo=37830): Corrected how [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) and [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) compile inside a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block whenever the matching [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) block holds a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) carrying a non-constant value.

[bpo-37474](https://bugs.python.org/issue?@action=redirect&bpo=37474): Under FreeBSD, Python has stopped invoking `fedisableexcept()` during startup to govern the floating-point control mode. That invocation has been pointless ever since FreeBSD 6, where it became the standard mode.

[bpo-37543](https://bugs.python.org/issue?@action=redirect&bpo=37543): Made pymalloc faster for a non PGO build.

[bpo-37414](https://bugs.python.org/issue?@action=redirect&bpo=37414): The undocumented `sys.callstats()` function is gone. Starting with Python 3.7 it had been deprecated and consistently returned `None`. It depended on a special build option, `CALL_PROFILE`, which had itself already been dropped in Python 3.7.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
