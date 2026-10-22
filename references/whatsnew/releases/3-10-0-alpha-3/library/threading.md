# Python 3.10.0 alpha 3 / library / threading

[bpo-42350](https://bugs.python.org/issue?@action=redirect&bpo=42350): Correct the [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) class behaviour at fork: take no action when the thread has already stopped (for instance, a fork happening at Python exit). Formerly an error appeared in the child process log.

[bpo-42308](https://bugs.python.org/issue?@action=redirect&bpo=42308): Add [`threading.__excepthook__`](https://docs.python.org/3.14/library/threading.html#threading.__excepthook__) so the original value of [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) can be recovered should it be replaced by a broken or otherwise different value. Mario Corchero wrote the patch.

[bpo-42251](https://bugs.python.org/issue?@action=redirect&bpo=42251): Added [`threading.gettrace()`](https://docs.python.org/3.14/library/threading.html#threading.gettrace) and [`threading.getprofile()`](https://docs.python.org/3.14/library/threading.html#threading.getprofile) for fetching the functions registered through [`threading.settrace()`](https://docs.python.org/3.14/library/threading.html#threading.settrace) and [`threading.setprofile()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile) in turn. Mario Corchero wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
