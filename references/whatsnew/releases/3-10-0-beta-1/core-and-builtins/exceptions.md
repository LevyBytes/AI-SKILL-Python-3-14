# Python 3.10.0 beta 1 / core and builtins / exceptions

[bpo-42609](https://bugs.python.org/issue?@action=redirect&bpo=42609): Stopped the AST validator and optimizer from crashing while compiling preposterously long expressions such as `"+0"*1000000`. They now raise [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) in those cases.

[bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530): On an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), `PyErr_Display()` now proposes close attribute names taken from the object where the exception originated. Pablo Galindo wrote the patch

[bpo-43914](https://bugs.python.org/issue?@action=redirect&bpo=43914): Rather than pointing only at the spot where trouble was detected, [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions coming from the interpreter now mark the complete span of the offending expression. Pablo Galindo wrote the patch.

[bpo-43859](https://bugs.python.org/issue?@action=redirect&bpo=43859): Sharpen the message produced for [`IndentationError`](https://docs.python.org/3.14/library/exceptions.html#IndentationError) exceptions. Pablo Galindo wrote the patch

[bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530): For a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) the interpreter throws, `PyErr_Display()` now proposes look-alike variable names drawn from the function where the exception originated. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
