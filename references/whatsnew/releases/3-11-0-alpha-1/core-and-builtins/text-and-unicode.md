# Python 3.11.0 alpha 1 / core and builtins / text and unicode

[bpo-41972](https://bugs.python.org/issue?@action=redirect&bpo=41972): Adjusted the string-searching algorithm in fastsearch.h so most cases run through a shorter inner loop.

[bpo-1514420](https://bugs.python.org/issue?@action=redirect&bpo=1514420): While formatting an exception, the interpreter no longer tries to open files whose names sit in angle brackets (such as “&lt;string&gt;” or “&lt;stdin&gt;”).

[bpo-43667](https://bugs.python.org/issue?@action=redirect&bpo=43667): Better Unicode handling in non-UTF locales running on Oracle Solaris. Other Solaris systems are not affected by this issue.

[bpo-44156](https://bugs.python.org/issue?@action=redirect&bpo=44156): The string caches inside `compile.c` are now compatible with subinterpreters.

[bpo-28307](https://bugs.python.org/issue?@action=redirect&bpo=28307): The compiler now optimizes plain C-style formatting whose literal format holds only the format codes %s, %r and %a, rewriting them into f-string expressions.

[bpo-44396](https://bugs.python.org/issue?@action=redirect&bpo=44396): Fixed a potential crash in the tokenizer while it raised syntax errors over unclosed strings. Pablo Galindo authored the patch.

[bpo-45190](https://bugs.python.org/issue?@action=redirect&bpo=45190): Refresh the Unicode databases to Unicode 14.0.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
