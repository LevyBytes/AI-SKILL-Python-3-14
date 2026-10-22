# What's New In Python 3.6 / Notable changes in Python 3.6.4

### Notable changes in Python 3.6.4

Belonging once to the public API, the `PyExc_RecursionErrorInst` singleton has been dropped, because its members were never cleared and that could provoke a segfault as the interpreter was shutting down. (Contributed by Xavier de Gaye in [bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898) and [bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697).)

[Subject index](INDEX.md) · [Previous source section](removal-of-make-touch-build-target.md) · [Next source section](notable-changes-in-python-3-6-5.md) · [Release/subject declaration](summary-release-highlights.md)
