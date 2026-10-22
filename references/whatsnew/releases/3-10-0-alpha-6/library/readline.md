# Python 3.10.0 alpha 6 / library / readline

[bpo-42819](https://bugs.python.org/issue?@action=redirect&bpo=42819): [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline): Turn bracketed paste off explicitly in the interactive interpreter, regardless of whether it is set in the inputrc, on by default (for example GNU Readline 8.1), or switched on when a user invokes `readline.read_init_file()`. Bracketed paste support has not landed in the Python REPL. Bracketed mode additionally emits the `"\x1b[?2004h"` escape sequence to stdout, which triggers test failures in applications lacking support for it. Enabling it explicitly remains possible via `readline.parse_and_bind("set enable-bracketed-paste on")`. Dustin Rodrigues wrote the patch.

[bpo-43172](https://bugs.python.org/issue?@action=redirect&bpo=43172): When compiled straight against libedit, the readline module now succeeds in its test suite. The behavior of [`readline.get_begidx()`](https://docs.python.org/3.14/library/readline.html#readline.get_begidx) together with [`readline.get_endidx()`](https://docs.python.org/3.14/library/readline.html#readline.get_endidx) still carries unavoidable API differences that depend on whether libreadline or libedit is in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
