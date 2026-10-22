# Python 3.5.0 alpha 2 / library / popen object inside statement no longer strands zombie exit

[bpo-21619](https://bugs.python.org/issue?@action=redirect&bpo=21619): A Popen object inside a with statement no longer strands a zombie on exit when the pipe broke. Martin Panter contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
