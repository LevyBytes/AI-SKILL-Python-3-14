# What’s New In Python 3.8 / threading — threading

### threading

A new [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) function arrived that deals with an uncaught [`threading.Thread.run()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.run) exception. You can override it to govern how uncaught `threading.Thread.run()` exceptions get handled. (Contributed by Victor Stinner in [bpo-1230540](https://bugs.python.org/issue?@action=redirect&bpo=1230540).)

A new [`threading.get_native_id()`](https://docs.python.org/3.14/library/threading.html#threading.get_native_id) function arrived together with a [`native_id`](https://docs.python.org/3.14/library/threading.html#threading.Thread.native_id) attribute on the [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) class. Each one yields the kernel-assigned native integral Thread ID belonging to the running thread. The capability exists only on some platforms; consult `get_native_id` for further details. (Contributed by Jake Tesler in [bpo-36084](https://bugs.python.org/issue?@action=redirect&bpo=36084).)

[Subject index](INDEX.md) · [Previous source section](tarfile.md) · [Next source section](tokenize.md) · [Release/subject declaration](assignment-expressions.md)
