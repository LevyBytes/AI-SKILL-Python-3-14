# Python 3.10.0 alpha 2 / core and builtins / exceptions

[bpo-41659](https://bugs.python.org/issue?@action=redirect&bpo=41659): Squashed a parser defect where a curly brace trailing a `primary` failed to error out at once. As a result, malformed expressions such as `a {b}` raised a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) carrying an incorrect offset, while malformed expressions that ended with a curly brace like `a {` would not error immediately inside the REPL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
