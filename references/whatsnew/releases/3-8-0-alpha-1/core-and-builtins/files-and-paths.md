# Python 3.8.0 alpha 1 / core and builtins / files and paths

[bpo-30455](https://bugs.python.org/issue?@action=redirect&bpo=30455): The C code, the Python code, and the token-related documentation are now produced from one single source file `Grammar/Tokens`.

[bpo-33451](https://bugs.python.org/issue?@action=redirect&bpo=33451): Close directly executed pyc files ahead of any call to `PyEval_EvalCode()`.

[bpo-32492](https://bugs.python.org/issue?@action=redirect&bpo=32492): Make `namedtuple()` attribute access 1.6x faster via a C fast-path for the name descriptors. Patch by Pablo Galindo.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
