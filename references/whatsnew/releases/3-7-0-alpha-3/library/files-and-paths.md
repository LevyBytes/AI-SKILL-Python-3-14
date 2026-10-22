# Python 3.7.0 alpha 3 / library / files and paths

[bpo-32110](https://bugs.python.org/issue?@action=redirect&bpo=32110): For non-negative *n*, `codecs.StreamReader.read(n)` now hands back at most *n* characters/bytes. That brings it in line with the `read()` methods on other file-like objects.

[bpo-21862](https://bugs.python.org/issue?@action=redirect&bpo=21862): The cProfile command line now takes `-m module_name` as a substitute for a script path. Sanyam Khurana wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
