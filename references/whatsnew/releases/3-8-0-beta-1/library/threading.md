# Python 3.8.0 beta 1 / library / threading

[bpo-1230540](https://bugs.python.org/issue?@action=redirect&bpo=1230540): Supplies a fresh [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) function that copes with an uncaught [`threading.Thread.run()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.run) exception. You can override it to steer how uncaught `threading.Thread.run()` exceptions get treated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
