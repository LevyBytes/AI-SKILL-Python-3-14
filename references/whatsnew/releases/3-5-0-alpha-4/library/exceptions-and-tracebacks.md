# Python 3.5.0 alpha 4 / library / exceptions and tracebacks

[bpo-23811](https://bugs.python.org/issue?@action=redirect&bpo=23811): Supply the absent newline on the PyCompileError error message. Alex Shkop wrote the patch.

[bpo-23400](https://bugs.python.org/issue?@action=redirect&bpo=23400): When sem_open is missing, the same exception is now raised under both Python 2 and 3. Davin Potts wrote the patch.

[bpo-23485](https://bugs.python.org/issue?@action=redirect&bpo=23485): select.select() now retries by itself using the recomputed timeout after a signal interrupts it, unless the signal handler raises an exception. This belongs to [**PEP 475**](https://peps.python.org/pep-0475/).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
