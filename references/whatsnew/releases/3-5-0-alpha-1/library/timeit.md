# Python 3.5.0 alpha 1 / library / timeit

[bpo-2527](https://bugs.python.org/issue?@action=redirect&bpo=2527): The timeit functions gain a *globals* argument that lets you replace the globals namespace where the measured code runs. Ben Roberts wrote the patch.

[bpo-18518](https://bugs.python.org/issue?@action=redirect&bpo=18518): timeit now turns away statements that can't compile outside a function or a loop (for example "return" or "break").

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
