# Python 3.9.0 beta 1 / library / threads and concurrency

[bpo-40453](https://bugs.python.org/issue?@action=redirect&bpo=40453): A keyword-only `isolated=True` parameter is now offered by `_xxsubinterpreters.create()`. Such an isolated subinterpreter is barred from launching threads, starting a child process, or invoking `os.fork()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
