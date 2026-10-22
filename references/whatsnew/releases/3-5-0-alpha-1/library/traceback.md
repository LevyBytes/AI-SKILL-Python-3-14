# Python 3.5.0 alpha 1 / library / traceback

[bpo-9815](https://bugs.python.org/issue?@action=redirect&bpo=9815): When an exception’s traceback holds local variables, assertRaises now attempts to release the references to them.

[bpo-17442](https://bugs.python.org/issue?@action=redirect&bpo=17442): Within its showtraceback method, InteractiveInterpreter now shows the entire chained traceback, matching the built in interactive interpreter.

[bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911): A fresh object API for traceback arrives, which can skip looking up lines entirely until the traceback truly gets rendered, and which avoids holding any of the original objects alive.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
