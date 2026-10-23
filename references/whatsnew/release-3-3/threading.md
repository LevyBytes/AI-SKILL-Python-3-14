# What's New In Python 3.3 / threading - threading

### threading

[`threading.Condition`](https://docs.python.org/3.14/library/threading.html#threading.Condition), [`threading.Semaphore`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore), [`threading.BoundedSemaphore`](https://docs.python.org/3.14/library/threading.html#threading.BoundedSemaphore), [`threading.Event`](https://docs.python.org/3.14/library/threading.html#threading.Event), and [`threading.Timer`](https://docs.python.org/3.14/library/threading.html#threading.Timer) ? each formerly a factory function that handed back a class instance ? are real classes now and accept subclassing. ?ric Araujo contributed this; refer to [bpo-10968](https://bugs.python.org/issue?@action=redirect&bpo=10968).

A `daemon` keyword argument is now accepted by the [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) constructor, letting you override the inherited `daemon` flag value that would otherwise come from the parent thread ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)).

What used to be the private `_thread.get_ident` is now exposed publicly as [`threading.get_ident()`](https://docs.python.org/3.14/library/threading.html#threading.get_ident). That removes a number of spots in the stdlib that reached straight into the `_thread` module. Outside code that relied on `_thread.get_ident` ought to switch to this new public entry point as well.

[Subject index](INDEX.md) · [Previous source section](textwrap.md) · [Next source section](time.md) · [Release/subject declaration](summary-release-highlights.md)
