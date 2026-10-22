# Python 3.8.0 beta 1 / core and builtins / text

[bpo-36817](https://bugs.python.org/issue?@action=redirect&bpo=36817): Introduces a `=` f-string feature aimed at debugging. It may sit ahead of `!s`, `!r`, or `!a`. The output is the expression's text, then an equal sign, then the repr of the expression's value. Thus `f'{3*9+15=}'` would match the string `'3*9+15=42'`. Supplying `=` makes the default conversion `!r`, except when a format spec appears, in which case the formatting stays as is and __format__ does the work.

[bpo-36878](https://bugs.python.org/issue?@action=redirect&bpo=36878): Whatever text follows a `# type: ignore` comment is now retained in the AST. To illustrate, a type ignore written `# type: ignore[E1000]` ends up with the string `"[E1000]"` recorded in its AST node.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
