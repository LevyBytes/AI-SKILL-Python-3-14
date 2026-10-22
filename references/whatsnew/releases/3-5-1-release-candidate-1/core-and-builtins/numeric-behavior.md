# Python 3.5.1 release candidate 1 / core and builtins / numeric behavior

[bpo-24802](https://bugs.python.org/issue?@action=redirect&bpo=24802): Stopped buffer overreads whenever int(), float(), compile(), exec() and eval() receive bytes-like objects. Such objects need not be terminated by a null byte, yet these functions had presumed they were.

[bpo-25131](https://bugs.python.org/issue?@action=redirect&bpo=25131): Made the line number and column offset for set/dict literals and comprehensions line up with the opening brace.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
